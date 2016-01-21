s="""
.a.a.fy
	int x_a = 10
	int y_a = 20

.b.fy
	import .a.a(
		x_a, 
		y_a = y,
	)

	int x = 1

	print 'in b {:x} {:x_a} {:y}'

"""

from fython.test import *

shell('rm -rf a/ a.* b.* c.*')

writer(s)

w = load('.b', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
