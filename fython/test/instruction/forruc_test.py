s = r"""
.a.fy
	integer: i j x y

	for i in [1, 2]:
		x += 1
		for j in [1, 2]:
			y -= 2

	# print '{:x} {:y}'
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
