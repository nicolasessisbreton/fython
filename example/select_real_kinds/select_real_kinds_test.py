s = """
.a.fy
	# taken from: https://gcc.gnu.org/onlinedocs/gfortran/SELECTED_005fREAL_005fKIND.html

	integer cons p6 = selected_real_kind(6)
	integer cons p10r100 = selected_real_kind(10,100)
	integer cons r400 = selected_real_kind(r=400)

	real(kind=p6) x
	real(kind=p10r100) y
	real(kind=r400) z

	print '{:precision(x)} {:range(x)}'
	print '{:precision(y)} {:range(y)}'
	print '{:precision(z)} {:range(z)}'
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=1)
print(open(w.module.url.fortran_path, 'r').read())
