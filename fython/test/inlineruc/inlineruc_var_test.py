s="""
.a.fy
	real x=10

	def f:
		inline x
		print 'x {:s}'

	f()
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
