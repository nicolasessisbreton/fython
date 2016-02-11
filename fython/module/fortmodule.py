from pickle import dump, HIGHEST_PROTOCOL
from ..config import *

pickable_field = [
	'url',
	'value',
]

class FortModule(Data):
	is_fymodule = 0
	is_fortmodule = 1
	is_somodule = 0

	def __init__(s, url, stack):
		s.url = url
		s.value = url.dotted
		s.module = url.fy_parent
		s.stack = stack
		s.dependency = []		
		
	def resolve(s):
		pass		
		
	def write_fortran(s):
		pass	

	def save(s):
		dump(
			s, 
			open(s.url.pickle, 'wb'), 
			protocol = HIGHEST_PROTOCOL, 
		)

	def compile_fortran(s):
		cmd = """
			cd {cache_dir:s}
			{fortran_compiler:s} {target_name:s} {cflag:s} {includedir_flag:s} -fpic -c
		""".format(
			cache_dir = s.url.fycache_dir,
			fortran_compiler = fyfc.cmd,
			target_name = s.url.path,
			cflag = s.stack.cflag,
			includedir_flag = s.stack.includedir_flag,
		)

		out, error = shell(cmd)

		if error:
			if fyfc.is_error(out):
				s.module.throw(err.compilation_error, cmd=trim(cmd), compilation_error=out)	
			else:
				print(out)

	def __getstate__(s):
		r = {}
		for key, item in s.__dict__.items():
			if key in pickable_field:
				r[key] = item
		return r

	def __setstate__(s, state):
		for key, item in state.items():
			s.__dict__[key] = item
