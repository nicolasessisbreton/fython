s="""
.a.fy
	def f:
		int in x
		int in y
.b.fy
	import .a(*)

	def f:
		print 'x y {:x} {:y}'

	f(1, 2)

"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.b', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
