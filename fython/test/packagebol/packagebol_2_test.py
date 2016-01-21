s = """
.a.fy
	class A:
		real x

		def lt:
			s in
			A in other
			bool res r
			r = s.x < other.x

.b.fy
	import type_provider(T)

	def quicksort:
		T dimension(10) in x
		int: i r
		for i in [1, 10]:
			r = x[i].lt( x[i+1] )
			print 'i {:r}'

.c.fy
	import .a(*)

	import .b(*)
	|| type_provider=.a, T=A ||

	A dimension(10) a
	int i

	for i in [1, 10]:
		a.x = i

	quicksort(a)
"""

from fython.test import *

shell('rm -rf a/ a.* b.* c.*')

writer(s)

w = load('.c', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
