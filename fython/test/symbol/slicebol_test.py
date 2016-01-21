s = r"""
.a.fy
	integer: x(10) y(10, 10, 10)
	x[3:5] = 2

	x[2:7] = sum( y[1:2, 2:5, 6:7] )
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
