from textwrap import indent as add_indent

tab = '\t'

class Buffer:
	def __init__(s, r='', newline='\n'):
		s.r = str(r)
		s.tab = ''
		s.newline = newline

	# !=: append exactly the target
	def __ne__(s, other):
		s.r += str(other)
		return s
		
	# &=: append space, then target, without newline
	def __iand__(s, other):
		s.r += ' ' + str(other)
		return s

	# +=: append + newline
	def __iadd__(s, other):
		s.r += str(other) + s.newline + s.tab
		return s

	# *=: append block, maintaining indent		
	def __mul__(s, other):
		s.rstrip(s.tab)
		s.r += add_indent(str(other), s.tab)
		return s

	# call with formats
	def __call__(s, source, *args, **kwargs):
		s.r += source.format(*args, **kwargs) + s.newline + s.tab
		return s

	def __str__(s):
		return s.r

	def __format__(s, fmt):
		return s.r

	def rcut(s, n):
		s.r = s.r[:-n]

	def rstrip(s, x):
		s.r = s.r.rstrip(x)

	@property
	def has_content(s):
		return s.r != ''

	@property
	def indent(s):
		s.tab += tab
		s.r += tab

	@property
	def dedent(s):
		s.tab = s.tab[:-1]
		s.r.rstrip(tab)

	def __repr__(s):
		a = ''
		for x in s.r:
			if x != '':
				a = x
				break

		b = ''
		for x in s.r:
			if x != '':
				b = x
				break

		if a == '' and b == '':
			r = 'Buffer(\'\')'

		elif a !='' and b == '':
			r = 'Buffer({:s})'.format(a)

		elif a =='' and b != '':
			r = 'Buffer({:s})'.format(b)

		else:
			r = 'Buffer({:s}>{:s}'.format(a, b)

		return r

	@property
	def rep(s):
		return s.__repr__()

	@property
	def nfo(s):
		return repr(s.r)

	def rreplace(s, old, new):
		if s.r.endswith(old):
			s.r = s.r.rstrip(old)
			s.r += new
			