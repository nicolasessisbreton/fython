from ..config import *

class StrResolver:
	def __init__(s, dotbol):
		s.dotbol = dotbol
		s.args = dotbol.args
		s.module_ast = dotbol.module.ast[0]
		s.module_name = dotbol.module.name[0]
		s.klass = 0
		s.ndx = 0
		s.b = Buffer(newline='%')
		s.n = len(dotbol.args)

		s.modules = dotbol.module.stack.module

		# bootstrap	
		x = dotbol.args[0]
		s.alias = x.value
		s.target = x.ast_target

	@property
	def advance(s):
		s.ndx += 1
		if s.ndx == s.n:
			# no more qualifier, finished
			return

		s.alias = s.args[s.ndx].value
		
		if s.klass:
			if s.alias in s.klass.ast:
				s.target = s.klass.ast[s.alias]

			elif s.dotbol.is_iruc_target and s.is_last_ndx and setpfx + s.alias in s.klass.ast:
					s.alias = setpfx + s.alias
					s.target = s.klass.ast[s.alias]
					s.target.used_as_pset = 1

			elif getpfx + s.alias in s.klass.ast:
				s.alias = getpfx + s.alias
				s.target = s.klass.ast[s.alias]
				s.target.used_as_pget = 1

			else:
				s.dotbol.throw(
					err.cannot_find_attribute_in_class, 
					class_name = s.klass.value, 
					attribute = s.alias,
				)


		else:
			s.target = s.module_ast[s.alias]

	@property
	def cargs(s):
		return s.args[s.ndx]

	@property
	def nfo(s):
		r = repr(s) + '\n'
		for key, item in s.__dict__.items():
			r += '\t{:s} {:s}\n'.format(key, repr(item))

		return r

	@property
	def rep(s):
		return s.__repr__()

	def __repr__(s):
		return 'StrResolver({:s})'.format(s.dotbol.url_value)

	@property
	def module(s):
		pass

	@module.setter
	def module(s, module):
		s.module_ast = module.ast[0]
		s.module_name = module.name[0]

	@property
	def is_last_ndx(s):
		return s.ndx == s.n - 1