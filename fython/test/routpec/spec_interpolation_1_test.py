s="""
.a.fy
	def f:
		int in x
		int in y

	def spec(f) g:
		print 'x y {:x} {:y}'

	g(1, 2)

"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
