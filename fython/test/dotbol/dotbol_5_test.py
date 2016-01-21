s = r"""
.a.fy
	class A:
		real u = 1

		real z

		def pget x:
			s in
			real res r
			r = s.z

		def pset x:
			s inout
			real in value
			s.z = value

	class B:
		A a

	class C:
		B b

	class D:
		C c


	D d	
	d.c.b.a.x = 10.

	print '{:d.c.b.a.u} {:d.c.b.a.x}'
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())

