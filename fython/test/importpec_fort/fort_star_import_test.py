s="""
.a.f90
	module a
		integer :: x_a = 10
	end module

.b.fy
	import .a(*)

	int x = 1

	print 'in b {:x} {:x_a}'

"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.b', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
