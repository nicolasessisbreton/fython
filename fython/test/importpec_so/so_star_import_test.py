s="""
.a.f90
	module a

		contains

			function x_a() result(r) bind(c)
				real r
				r = 10
			end function

	end module

.b.fy
	import .a_so(*)

	interface:
		def iso(c) x_a:
			real res r

	int x = 1

	print 'in b {:x} {:x_a()}'

"""

from fython.test import *

shell('rm -rf a.* *.so')

writer(s)

shell('ifort -shared -fpic a.f90 -o a_so.so')

w = load('.b', force=1, release=1, verbose=0, run_main=0)
print(open(w.module.url.fortran_path, 'r').read())
