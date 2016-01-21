s = r"""
.a.fy
	int dimension(10) target x
	int dimension(:) pointer y
	y => x[3:5]
"""
from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
