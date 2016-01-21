s = """
.a.fy
	real dimension(:) allocatable: x y z
	integer: 
		a=1 
		b=1 
		c=1 
		n=1 
		m=1

	alloc x(n)
	dealloc x

	alloc(n) x
	dealloc x


	alloc: x(a) y(b) z(c)
	dealloc: x y z

	alloc(n): x y(m) z
	dealloc: x y z

	alloc:
		x(a)
		y(b)
		z(c)

	dealloc:
		x
		y
		z

	alloc(n):
		x
		y(m)
		z

	dealloc:
		x
		y
		z
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())

