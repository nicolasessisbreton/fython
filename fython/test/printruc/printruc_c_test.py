s = r"""
.a.fy
	int x
	print c 'start '
	print c 'in a {:x}'
	print ' end'
	print 'new'
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
