s = """
.a.fy
	real x = 1
	real y = 10

	def f:
		real in x
		real in y
		print '{:x} {:y}'

	f(y=1.)
	f()
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())

