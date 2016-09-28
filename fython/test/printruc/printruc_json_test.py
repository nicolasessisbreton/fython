s = r"""
.a.fy
	int:
		x
		y(2)

	x = 0
	y = 1

	print 'jn {jn:x}'
	print 'j {j:x}'
	print 'jv {jv:y}'
	print 'jvn {jvn:y}'
	print 'jn_a {jn_a:x}'
	print 'j_a {j_a:x}'
	print 'jv_a {jv_a:y}'
	print 'jvn_a {jvn_a:y}'
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=1)
# print(open(w.module.url.fortran_path, 'r').read())
