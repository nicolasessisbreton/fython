s="""
.a.fy
	class A:
		def f:
			self in
			print 'f from A'

	class B(A):
		pass
		
	B b
	b.f()
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
