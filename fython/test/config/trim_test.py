from fython.config import *
from numpy.testing import *

def p(s, e):
	r = trim(s)
	print(repr(r))
	assert_equal(r, e)

'\nis without\nleading space\nbeginning\nend\n'

p("""
	a
	b
	c
""",
'a\nb\nc',
)


p("""
	a
	b
	c
	
""",
'a\nb\nc\n'
)

p('''
	
	is without
	leading space
	beginning
	end
	
''',
'\nis without\nleading space\nbeginning\nend\n'
)
