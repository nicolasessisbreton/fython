s = r"""
.a.fy
	class employee:
		int x
		
	def f:
		real in dimension(:) x
		employee inout z
		real pointer : a b c
		int cons n=10
		real:
			u
			v(n)
			w
		real res r
		r += u
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
