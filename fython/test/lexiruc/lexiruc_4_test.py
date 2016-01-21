s = """
.a.fy
	def temp f:
		real in x
		T r
		r = x
		print '{:r}'

	def g = f(
		T = int,
	)

	g(10.)
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
