s="""
.a.fy
	import iso_c_binding(*)
	print '1'
"""

from fython.test import *

use_gfortran()

writer(s)

w = load('.a', force=1, release=1, verbose=0)

use_ifort() # back to ifort