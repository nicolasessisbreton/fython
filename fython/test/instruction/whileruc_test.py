s = r"""
.a.fy
	int x=10
	while x >1:
		x += 1
		while x>1 and true or false and not False:
			x -= 2
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
