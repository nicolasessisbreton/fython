class Lexem:
	def __init__(s, type, lineno, unit):
		s.type = type
		s.lineno = lineno
		s.value = unit
		
	def __repr__(s):
		return 'Lexem({:d}, {:s})'.format(s.lineno, repr(s.value.value))

	@property
	def nfo(s):
		r = repr(s) + '\n'
		for key, item in s.__dict__.items():
			r += '\t{:s} {:s}\n'.format(key, repr(item))

		return r

	@property
	def rep(s):
		return s.__repr__()


	def clone(s, module):
		unit = s.value.clone(module)
		x = Lexem(s.type, s.lineno, unit)
		return x