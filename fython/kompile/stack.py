import re
from collections import OrderedDict
from ..config import *
from fython.module import *
from ..package_interpolation import *

ifort_position_re = re.compile('^\-*\^$', re.MULTILINE)

class Stack(Data):
	def __init__(
		s,
		release,
		cwd,
		force,
		verbose,
	):
		s.release = release
		s.debug = not release
		s.cwd = cwd
		s.force = force
		s.verbose = vb.Verbose(verbose)

		# all loaded module
		s.module = {}
		s.fort = {}

		# compilation
		s.includedir = OrderedDict()
		s.object_path = OrderedDict()
		s.need_link = 0
		s.includedir_flag = ''
		s.object_path_flag = ''	

		if s.release:
			s.cflag = fyfc.release
			
		else:
			s.cflag = fyfc.debug

		# helper
		s.package_interpolation = Package_Interpolation()
		
	# module
	def load(s, url, cwd, is_target=0):
		if not isinstance(url, Url):
			url = Url(
				url = url,
				cwd = cwd,
				ext = exts.importable,
				release = s.release,
			)

		if url.pickle in s.module:
			return s.module[url.pickle]
			# nothing to do ; already loaded

		elif s.is_up_to_date(url):
			m = restore_module(url, s)
			m.is_up_to_date = 1

		else:
			m = get_module(url, s)
			m.is_up_to_date = 0

		s.module[m.url.pickle] = m

		# run
		if m.is_up_to_date:
			for url in m.dependency:
				s.load(url, cwd)

		else:
			s.need_link = 1

			m.resolve()
			
			m.write_fortran()
			m.compile_fortran()

			m.save()

		s.add_includedir(m.url.fycache_dir)
		s.add_object(m.url.object_path)	

		if is_target:
			s.target = m

		elif m.url.dotted == fytbk.url:
			s.fytbk = m

		return m

	def is_up_to_date(s, url):
		if s.force and url.dotted != fytbk.url:
			return 0
		else:
			return url.is_up_to_date

	# compilation
	def add_includedir(s, path):
		if path not in s.includedir:
			p = ' -I' + path
			s.includedir[path] = 0
			s.includedir_flag += p

	def add_object(s, path):
		if path not in s.object_path:
			p = ' ' + path
			s.object_path[path] = 0
			s.object_path_flag += p

	def link(s):
		cmd = """
			cd {cache_dir:s}
			{fortran_compiler:s} -shared -fpic -o {program_name:s} {object_path_flag:s}
		""".format(
			cache_dir = s.target.url.fycache_dir,
			fortran_compiler = fyfc.cmd,
			program_name = s.target.url.so_name,
			object_path_flag = s.object_path_flag,
		)

		out, error = shell(cmd)

		if error:
			out = s.reveal_guid(out)

			if fyfc.is_error(out):
				s.target.throw(
					err.linking_error, 
					cmd = trim(cmd), 
					linking_error =out,
				)

			else:
				print(out)

	def reveal_guid(s, source):
		for _, m in s.module.items():
			if m.is_fymodule:
				source = source.replace(m.module_guid, m.value)
				source = source.replace('! ' + m.value, '')

				for guid, name in m.guid.items():
					source = source.replace(guid, name)
					source = source.replace(guid.upper(), name)

		source = ifort_position_re.sub('', source)

		return source	