s = r"""
.a.fy
	integer: x=1, y=3
	if x > 4 and y < 5:
		if x:
			y += 6

	elif x<7:
		x = 8

	else:
		x=9
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
