s = r"""
.a.fy
	int x(10)
	print 'x {vc:x} end'
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
