import sys
from os.path import exists
from pickle import load
from collections import OrderedDict
from pickle import dump, HIGHEST_PROTOCOL
from importlib import import_module
from ..config import *
from ..resolve import resolve
from ..lex import *
import fython.traceback as tbk
from ..yacc import *
from ..pywrapper import *
from .sourcemodule import SourceModule

pickable_field = [
	'is_lexical_interpolation_module',
	'module_guid',
	'ast', 
	'name', 
	'guid',
	'dependency', 
	'is_module',
	'is_class',
	'is_varpec',
	'is_routpec',

	'url', 
	'value',
	'source',
	'source_lines',
	'line_offset',

	'receiver',
	'main_buffer',
]

guid_tag_start = '<a8o4j<' # salted to avoid collision
guid_tag_end = '>a8o4j>' # salted to avoid collision
guid_tag_len = len(guid_tag_start)

guid_tag_re = re.compile('{:s}.*?{:s}'.format(guid_tag_start, guid_tag_end))

class FyModule:
	is_fymodule = 1
	is_fortmodule = 0
	is_somodule = 0

	def __init__(s, is_lexical_interpolation_module=0):
		s.is_lexical_interpolation_module = is_lexical_interpolation_module
		
		s.module_guid = gen_guid()

		# table ; innerest frame last
		s.ast = [{}] # name > entity ast
		s.name = [{}] # name > guid
		s.contains_used = [0] # against rout
		s.klass = [0]	
		s.tbk_frame_rout = ['main']
		s.level = 0
		s.frame_guid =[s.module_guid]
		s.all_frame = {s.module_guid:s.name[0]}

		s.guid = {} # guid > name ; global over all frame
		s.dependency = [] # url


		# production
		s.module_buffer = Buffer(implicit_none) # module buffer
		s.main_buffer = Buffer()
		s.method_buffer = Buffer()

		# dependency
		s.dependency = []

		# helper
		s.receiver = 0
		s.method_buffer_enable = 0

		s.is_module = 1
		s.is_class = 0
		s.is_varpec = 0
		s.is_routpec = 0

		s.tbk_mark_on = 1

	@property
	def tbk_mark_off(s):
		return not s.tbk_mark_on
		
	def throw(s, error, line=None, msg=None, return_only=None, **kwargs):
		b = Buffer()
		
		if msg:
			b += msg

		for key, item in kwargs.items():
			item = str(item)
			if '\n' in item or len(item) > 80:
				b += key
				b.indent
				b *= item
				b.dedent

			else:
				b += '{:s} {:s}'.format(key, item)

		if line:
			b += 'line {:d}'.format(line + s.line_offset)

		b += 'module {:s}'.format(s.value)

		if line:
			if line < len(s.source_lines):
				b += 'source'
				b.indent
				b *= s.source_lines[line-1]
				b.dedent

		if return_only:
			return error(b)

		else:
			raise error(b)
		
	# parsing work
	def input(s, source):
		pass
		# dummy to comply with yacc
		
	def token(s):
		if s.expanded_lexem:
			t = s.expanded_lexem.pop(0)
			return t

		if s.lexem:
			t = s.lexem.pop(0)
			expansion = s.expand_lexem(t)

			if expansion:
				t = expansion.pop(0)
				s.expanded_lexem[0:0] = expansion

			elif t.type == l.interpolationx:
				return s.token()	
				# interpolation produced nothing; must go to next token
				
			return t

	def expand_lexem(s, t):
		if t.type == l.interpolationx:
			u = t.value.value
			source = s.eval_interpolant(u)
			m = SourceModule(s, source, t.lineno)

			lex(m)

			r = s.adjust_interpolant_endian(m.lexem)

			# set module
			for i in range(len(r)):
				r[i].value.module = s

			return r

		elif t.type in [l.namex, l.funx, l.slicex]:
			u = t.value
			if u.is_interpolation_safe:
				u = u.value
				if u in s.package_interpolation:
					u = s.package_interpolation[u]
					r = []
					for x in u:
						if s.is_lexical_interpolation_module:
							r.append(x.clone(x.value.module))

						else:
							r.append(x.clone(s))

					# adjust if target was funx or slicex
					x = r[-1]
					if t.type == l.funx:
						if x.type == l.namex:
							module = x.value.module
							x.type = l.funx
							x.value = x.value.value # depromotion
							m = import_module('fython.lexem.funx')
							x.value = m.FunX(x, module = module)
							r[-1] = x

					elif t.type == l.slicex:
						if x.type == l.namex:
							module = x.value.module
							x.type = l.slicex
							x.value = x.value.value # depromotion
							m = import_module('fython.lexem.slicex')
							x.value = m.SliceX(x, module = module)
							r[-1] = x

					return r

	def eval_interpolant(s, code):
		try:
			s.interpolant._reset_cache()

			if '\n' in code or ';' in code:
				exec(
					code,
					s.interpolant.__dict__,
				)

				source = s.interpolant._write_cache

			else:
				source = eval(
						code,
						s.interpolant.__dict__,
					)

			source = str(source)
			
			return source

		except Exception as e:
			error = s.throw(
				err.error_in_interpolant, 
				py_error = repr(e), 
				interpolant = code,
				return_only = 1,
			)
			raise error from None

	def eval_import_statement(s, import_statement):
		s.has_py_dependency = 1
		try:
			exec(
				trim(str(import_statement)),	
				s.interpolant.__dict__,
			)

		except Exception as e:
			error = s.throw(
				err.python_import_error,
				import_error = repr(e), 
				import_statement = import_statement,
				return_only = 1,
			)
			raise error from None

	def adjust_interpolant_endian(s, r):
		# pop bofx, linefeedx, eox
		r = r[2:-1]
		if not r:
			return r 
			# r empty ; no lexem to import
			
		# adjust end
		last = r[-1]
		if last.value.unit == l.newlinex:
			r = r[:-1] # newlinex provided by next in s.lexem
		else:
			# pop newlinex in lexem
			if s.lexem[0].value.unit == l.newlinex:
				s.lexem.pop(0)

		return r	

	@property
	def package_interpolation(s):
		return s.stack.package_interpolation

	# entity management
	def add_ast(s, name, ast):
		s.ast[s.level][name] = ast

	def add_name(s, name):
		if s.level == 0:
			s.add_guided_name(name)

		else:
			s.add_solid_name(name)

	def add_guided_name(s, name):
		if name in s.previous_guid:
			guid = s.previous_guid[name]

		else:
			guid = gen_guid()

		s.name[0][name] = guid
		s.guid[guid] = name

		return guid

	def add_solid_name(s, name):
		s.name[s.level][name] = name

	# pickling
	def save(s):
		dump(
			s, 
			open(s.url.pickle, 'wb'), 
			protocol = HIGHEST_PROTOCOL, 
		)

	def __getstate__(s):
		r = {}
		for key, item in s.__dict__.items():
			if key in pickable_field:
				r[key] = item
		return r

	def __setstate__(s, state):
		for key, item in state.items():
			s.__dict__[key] = item

	def load_previous_guid(s):
		if s.stack.force or not exists(s.url.pickle):
			s.previous_guid = {}
			return

		p = load(open(s.url.pickle, 'rb')) # previous module
		s.module_guid = p.module_guid
		s.previous_guid = p.name[0]

	# parse
	def get_and_parse(s, url, stack):
		s.url = url
		s.value = url.dotted
		s.stack = stack	
		s.load_previous_guid()
		s.mangle_so_name()


		if s.value == fytbk.url:
			s.release = 1
			s.debug = 0

		else:
			s.release = stack.release
			s.debug = stack.debug

		s.verbose = stack.verbose

		s.source = open(s.url.path, 'r').read()
		s.source_lines = s.source.split('\n')
		s.line_offset = 0


		s.expanded_lexem = []

		import_module(fyinterpolant_url)
		s.interpolant = sys.modules.pop(fyinterpolant_url)

		lex(s)
		yacc(s)

			
	# wrapper
	def get_wrapper(s, run_main):
		w = PyWrapper(s, run_main)	
		return w

	# compilation
	def write_fortran(s):
		b = Buffer()

		b('module {:s} ! {:s}', s.module_guid, s.value)

		if s.value != fytbk.url:
			b += 'use ' + s.stack.fytbk.module_guid

		b += s.b

		if s.method_buffer.has_content:
			if not s.contains_used[0]:
				b += '\ncontains\n'
				s.contains_used[0] = 1
			b += s.method_buffer

		if s.main.has_content:
			if not s.contains_used[0]:
				b += '\ncontains\n'

			b += 'subroutine {:s}_main()'.format(s.module_guid)

			b.indent

			if s.debug:
				b != tbk.init_frame(s.value, 'main')

			b *= s.main

			if s.debug:
				b != tbk.del_frame()

			b.dedent
			
			b += 'end subroutine'

		b += 'end module'

		source = s.write_guid(str(b))

		open(s.url.fortran_path, 'w').write(source)

	def compile_fortran(s):
		if s.value == fytbk.url:
			cflag = fyfc.release
		else:
			cflag = s.stack.cflag

		cmd = """
			cd {cache_dir:s}
			{fortran_compiler:s} {target_name:s} {cflag:s} {includedir_flag:s} -fpic -c
		""".format(
			cache_dir = s.url.fycache_dir,
			fortran_compiler = fyfc.cmd,
			target_name = s.url.fortran_name,
			cflag = cflag,
			includedir_flag = s.stack.includedir_flag,
		)

		out, error = shell(cmd)

		if error:
			out = s.stack.reveal_guid(out)

			if fyfc.is_error(out):
				x = open(s.url.fortran_path, 'r').read()
				open(s.url.fortran_path, 'w').write(s.stack.reveal_guid(x))

				s.throw(
					err.compilation_error, 
					cmd = trim(cmd) +'\n', 
					fortran_code_path = s.url.fortran_path + '\n',
					compilation_error = out,
				)

			else:
				print(out)

	def resolve(s):
		for linecod in s.code:
			resolve(linecod)

	# frame management
	def add_frame(s):
		s.level += 1
		s.ast.append({})
		s.name.append({})
		s.contains_used.append(0)
		s.klass.append(0)
		s.tbk_frame_rout.append(0)

		guid = gen_guid()
		s.frame_guid.append(guid)
		s.all_frame[guid] = s.name[s.level]

	def pop_frame(s):
		s.level -= 1
		ast = s.ast.pop()	
		s.name.pop()
		s.contains_used.pop()
		s.klass.pop()
		s.tbk_frame_rout.pop()

		s.frame_guid.pop()

		return ast

	# dependency
	def add_fy_dependency(s, url):
		s.dependency.append(url)
		m = s.stack.load(url, s.url.module_dir)
		return m

	def add_fort_dependency(s, url):
		s.dependency.append(url.dotted)
		s.stack.load(url, s.url.module_dir)

	def add_so_dependency(s, url):
		s.dependency.append(url.dotted)
		s.stack.load(url, s.url.module_dir)

	def mangle_so_name(s):
		# to protect so cache	
		s.url.so_path = s.url.so_path.rstrip(s.url.so_name)
		s.url.so_name = s.module_guid + '.so'
		s.url.so_path += s.url.so_name


	def verbose_tag(s, tag):
		print('** {:s}: {:s} **'.format(s.value, tag))

	@property
	def has_main(s):
		return s.main.has_content

	def get_guid_tag(s, name):
		r = guid_tag_start	
		r += ':'.join(s.frame_guid)
		r += ':'
		r += name
		r += guid_tag_end
		return r

	def write_guid(s, source):
		r = guid_tag_re.sub(s.get_guid, source)

		if s.value == fytbk.url:
			return r

		# fytbk
		n = s.stack.fytbk.name[0]

		a = n[fytbk.init_frame]
		b = n[fytbk.del_frame]
		c = n[fytbk.advance_line]
		d = n[fytbk.int_to_char]

		r = r.replace(fytbk.init_frame_tag, a)
		r = r.replace(fytbk.del_frame_tag, b)
		r = r.replace(fytbk.advance_line_tag, c)
		r = r.replace(fytbk.int_to_char_tag, d)

		return r

	def get_guid(s, match):
		tag = match.group(0)[guid_tag_len:-guid_tag_len]
		frame_guid = tag.split(':')
		name = frame_guid.pop()

		for guid in frame_guid[::-1]:
			frame = s.all_frame[guid]
			if name in frame:
				return frame[name]

		return name

	def get_ast(s, name):
		for frame in s.ast[::-1]:
			if name in frame:
				return frame[name]

	def get_klass(s):
		for frame in s.klass[::-1]:
			if frame:
				return frame

	def __repr__(s):
		return 'FyModule({:s})'.format(s.value)

	@property
	def nfo(s):
		r = repr(s) + '\n'
		for key, item in s.__dict__.items():
			r += '\t{:s} {:s}\n'.format(key, repr(item))

		return r

	@property
	def rep(s):
		return s.__repr__()

	@property
	def b(s):
		if s.receiver:
			return s.receiver
		else:
			if s.method_buffer_enable:
				return s.method_buffer
			else:
				return s.module_buffer

	@property
	def main(s):
		if s.receiver:
			return s.receiver
		else:
			return s.main_buffer
	