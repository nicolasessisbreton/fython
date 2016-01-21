s="""
.a.fy
	class A:
		int x

		def f:
			s in
			print 'f from A {:s.x}'

	A a
	a.x = 10
	a.f()
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
