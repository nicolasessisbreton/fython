s="""
.c.a.py
	x = 10
	y = 20

.b.fy
	import .c.a(x, y=z)

	int x = |x| + |z|


	print 'in b {:x}'

"""

from fython.test import *

shell('rm -rf a c a.* b.*')

writer(s)

w = load('.b', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
