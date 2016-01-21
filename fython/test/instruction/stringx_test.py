s = """
.a.fy
	char(100) x
	char(3) dimension(2) y = ['abc', 'def']

	x = 'single line'

	x = "single line"

	x = '''
	newline
		tab
	'''

	# leading_space_trim
	x = '''
		is without
		leading space
		beginning
		end
	'''

	# if_want_begin_end_padding
	x = '''
		
		is without
		leading space
		beginning
		end
		
	'''
	# note above the consistent indentation, even for blank lines

	# multiline
	x = '''
	a
	b
	'''
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
