s="""
.a.fy
	class A:
		int x

.b.fy
	import .a(*)
	
	class A:
		int y

	A a
	a.x = 1
	a.y = 2

	print '{:a.x} {:a.y}'
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.b', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
