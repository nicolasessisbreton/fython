s="""
.a.fy
	class A:
		int x

	class B(A):
		int y

	B b
	b.x = 1
	b.y = 2

	print '{:b.x} {:b.y}'
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
