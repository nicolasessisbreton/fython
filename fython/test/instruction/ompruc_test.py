s = r"""
.a.fy
	integer: x r
	
	omp for reduction(+:r)

	omp:
		for, reduction(+:r)
		shared, private(x)
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
