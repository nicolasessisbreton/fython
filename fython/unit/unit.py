from importlib import import_module
from ..config import *
import fython.traceback as tbk
from .lexem import Lexem

class Unit:
	def __init__(s, t, module=None):
		s.lex_type = t.type
		s.value = t.value
		s.lineno = t.lineno		
		s.url_value = t.value	
		s.is_interpolation_safe = 1	
		s.lexem = [Lexem(type=t.type, lineno=t.lineno, unit=s)]		
		s.raw = []

		t.value = s

		if module:
			s.module = module
			
		else:
			s.module = t.lexer.module	

		# helper
		s.is_module = 0
		s.is_classpec = 0
		s.is_varpec = 0
		s.is_routpec = 0
		
		s.next_linecod = None
		s.previous_linecod = None

		s.guid_overwrite = 0
		
		s.is_klass_pset = 0
		s.is_iruc_target = 1
		
	def __format__(s, format):
		return str(s)

	def __str__(s):
		return s.value

	@property
	def newline(s):
		r = ' ! {:d}\n'.format(s.lineno)
		return r

	# tbk
	@property
	def tbk_frame(s):
		if s.module.debug:
			return tbk.init_frame(s.module.value, s.name.value)

		else:
			return ''

	@property
	def tbk_eframe(s):
		if s.debug:
			return tbk.del_frame()

		else:
			return ''

	@property
	def tbk_mark(s):
		if s.release:
			return ''

		elif s.module.tbk_frame_rout[s.level]:
			n = s.module.tbk_frame_rout[s.level]
			s.module.tbk_frame_rout[s.level] = 0
			return tbk.init_frame(s.module.value, n) + tbk.open_line(s.lineno)

		else:
			return tbk.open_line(s.lineno)

	@property
	def tbk_emark(s):
		if s.release:
			return ''
		else:
			return tbk.close_line()

	def throw(s,  error, **kwargs):
		return s.module.throw(
			error = error,
			line = s.lineno,
			**kwargs
		)

	def Buffer(s):
		return Buffer(newline = s.newline)


	# unit querying
	@property
	def nb_linecod(s):
		return len(s.linecod)
		
	@property
	def nb_modifier(s):
		return len(s.modifier)

	@property
	def is_bdotx(s):
		return s.unit == l.bdotx
	
	@property	
	def is_commax(s):
		return s.unit == l.commax

	@property
	def is_childcod(s):
		return s.unit == l.childcod
	
	@property
	def is_dotbol(s):
		return s.unit == l.dotbol

	@property
	def is_dedentx(s):
		return s.unit == l.dedentx

	@property
	def is_eofx(s):
		return s.unit == l.eofx

	@property
	def is_enumbol(s):
		return s.unit == l.enumbol

	@property
	def is_funbol(s):
		return s.unit == l.funbol

	@property
	def is_ibol(s):
		return s.unit == l.ibol

	@property
	def is_interpolationx(s):
		return s.unit == l.interpolationx

	@property	
	def is_ketbol(s):
		return s.unit == l.ketbol
		
	@property	
	def is_linefeedx(s):
		return s.unit == l.linefeedx
		
	@property
	def is_lpackagex(s):
		return s.unit == l.lpackagex

	@property
	def is_opbol(s):
		return s.unit == l.opbol
		
	@property
	def is_namex(s):
		return s.unit == l.namex	

	@property
	def is_numberx(s):
		return s.unit == l.numberx

	@property
	def is_newlinex(s):
		return s.unit == l.newlinex

	@property
	def is_rpackagex(s):
		return s.unit == l.rpackagex

	@property
	def is_rparx(s):
		return s.unit == l.rparx

	@property
	def is_rketx(s):
		return s.unit == l.rketx

	@property
	def is_semibol(s):
		return s.unit == l.semibol

	@property
	def is_semix(s):
		return s.unit == l.semix
		
	@property
	def is_slicebol(s):
		return s.unit == l.slicebol

	@property
	def is_stringx(s):
		return s.unit == l.stringx
	
	@property		
	def is_terminal(s):
		return s.unit in l.terminal

	@property
	def module_dir(s):
		return s.module.url.module_dir

	@property
	def modifier_only(s):
		t = s.modifier[-1]

		if t.is_childcod:
			r = s.modifier[1:-1]

		elif t.is_enumbol:
			r = s.modifier[1:-1]

		elif t.is_ibol:
			r = s.modifier[1:-1]
			

		elif t.is_newlinex:
			r = s.modifier[1:-2]

		else:
			s.throw(err.cannot_resolve_modifier)

		return r

	@property
	def modifier_and_atomic_target(s):
		r = s.modifier_only
		r.extend(s.atomic_target)
		return r

	@property
	def atomic_target(s):
		t = s.modifier[-1]

		r = []

		if t.is_childcod:
			for c in t.linecod:
				if c.has_ibol:
					r.append(c.modifier[0])
					
				else:
					r.extend(c.modifier[:-1])

		elif t.is_enumbol:
			r.extend(t.modifier)

		elif t.is_ibol:
			r.append(t)

		elif t.is_newlinex:
			r.append(s.modifier[-2])

		else:
			s.throw(err.cannot_resolve_modifier)

		return r

	@property
	def atomic_target_name_only(s):
		r = s.atomic_target
		for i in range(len(r)):
			t = r[i]
			if t.is_ibol:
				r[i] = t.target	

			elif t.is_opbol:
				r[i] = t.modifier[0]

		return r

	# url		
	def url(
		s, 
		url = None,
		cwd = None,
		ext = exts.importable,
		path_only = 0,
		skip_if_not_found = 0,
		packagebol = 0,
		release = None,
	):
		if url is None:
			url = s.url_value

		if cwd is None:
			cwd = s.module_dir
		
		if release is None:
			release = s.release	

		r = Url(
			url = url,
			cwd = cwd,
			ext = ext,
			path_only = path_only,
			skip_if_not_found = skip_if_not_found,
			packagebol = packagebol,
			release = release
		)

		return r
	
	# frame management	
	def add_frame(s):
		s.module.add_frame()

	def pop_frame(s):
		ast = s.module.pop_frame()
		return ast

	def add_ast(s, name, ast):
		s.module.add_ast(name, ast)

	def add_name(s, name):
		s.module.add_name(name)	

	@property
	def frame_ast(s):
		return s.module.ast[s.level]

	@property
	def frame_name(s):
		return s.module.name[s.level]

	@property
	def module_ast(s):
		return s.module.ast[0]

	@property
	def module_name(s):
		return s.module.name[0]

	# for lexical interpolation purpose
	def clone(s, module):
		token = Data()
		token.type = s.lex_type
		token.lineno = s.lineno
		token.value = s.value
		U = s.get_unit()
		c = U(token, module)

		return c

	@property
	def release(s):
		return s.module.release

	@property
	def debug(s):
		return s.module.debug

	@property
	def klass(s):
		return s.module.get_klass()

	def set_klass(s, klass):
		s.module.klass[s.level] = klass

	# classpec specific
	def get_method_name(s, name):
		r = '{class_name:s}_{routname:s}'.format(
			class_name = s.name,
			routname = name,
		)
		# the class name will be guided above
		
		return r

	@property
	def ast_target(s):
		return s.module.get_ast(s.value)

	def get_ast(s, alias):
		ast = s.module.get_ast(alias)
		if ast:
			return ast

		else:
			s.throw(err.cannot_find_targetted_ast, alias=alias)
		
	@property
	def childcod_target(s):
		return s.modifier[-1].linecod

	@property
	def cname(s):
		return s.__class__.__name__

	@property
	def nfo(s):
		r = repr(s) + '\n'
		for key, item in s.__dict__.items():
			r += '\t{:s} {:s}\n'.format(key, repr(item))

		return r

	@property
	def rep(s):
		return s.__repr__()
		
	# ^: add lexem ; add modifier raw
	def __xor__(s, unit):
		s.lexem.extend(unit.lexem)
		s.raw.append(unit)
		return s

	# print modifiers
	@property
	def repmod(s):
		r = ''
		for m in s.modifier:
			r += m.rep + ' '	
		return r

	# print args
	@property
	def repargs(s):
		for m in s.args:
			print(m.rep, end=' ')
		print('')

	# instruction buffer
	@property
	def b(s):
		return s.module.b
		
	@property
	def i(s):
		if s.level == 0:
			return s.module.main

		else:
			return s.module.b

	@property
	def level(s):
		return s.module.level

	@property
	def contains(s):
		if s.module.contains_used[s.level]:
			return ''

		else:
			s.module.contains_used[s.level] = 1
			return '\ncontains\n'

	@property
	def indent(s):
		s.module.b.indent
		s.module.main.indent

	@property
	def dedent(s):
		s.module.b.dedent
		s.module.main.dedent

	@property
	def redirect(s):
		pass

	@redirect.setter
	def redirect(s, receiver):
		s.module.receiver = receiver

	@property
	def contains_disable(s):
		s.module.contains_used[s.level] = 1

	def __repr__(s):
		if len(s.lexem) == 1:
			r = '{:s}({:d}, {:s})'.format(
				s.cname, 
				s.lineno, 
				str(s.lexem[0].value.value),
			)

		else:
			a = ''
			for x in s.lexem:
				if x.value.value != '':
					if not x.value.is_linefeedx:
						a = str(x.value.value)
						break

			b = ''
			for x in s.lexem[::-1]:
				if x.value.value != '':
					b = str(x.value.value)
					break

			r = '{:s}({:d}, {:s}>{:s})'.format(
					s.cname,
					s.lineno,
					a,
					b,
			)

		return r

	@property
	def modifier_only_direct_production(s):
		b = Buffer(newline='')
		for m in s.modifier_only:
			b != m
		return b

	@property
	def modifier_only_for_rout(s):
		return s.modifier_only[:-1]

	@property
	def childcod(s):
		return s.modifier[-1]

	def get_unit(s):
		c = s.cname
		x = c.lower()
		if c.endswith('X'):
			n = 'fython.lexem.' + x

		elif c.endswith('Bol'):
			n = 'fython.symbol.' + x

		else:
			n = 'fython.code.' + x

		m = import_module(n)
		u = getattr(m, c)

		return u

	# >: add import
	def __gt__(s, other):
		b = s.b
		b.rstrip(implicit_none)
		b != other 
		b != ';'
		b != implicit_none
		return s

	@property
	def method_buffer_enable(s):
		s.module.method_buffer_enable = 1

	@property
	def method_buffer_disable(s):
		s.module.method_buffer_enable = 0