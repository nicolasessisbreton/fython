s = r"""
.a.fy
	int x
	print 'in a {:x}'
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
