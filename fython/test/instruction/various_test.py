s = r"""
.a.fy
	real : x y z(10)
	int dimension(3) a = [1, 2, 3]
	
	x += 1 + 3

	x /=  sum(
		x +
		y +
		z	
	)

"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
