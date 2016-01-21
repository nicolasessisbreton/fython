s="""
.a.fy
	|
		write('''
			int x = 10
			if x > 0:
				print 'x is {{:x}}'
			else:
				print 'not reached'
		''')
	|
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
