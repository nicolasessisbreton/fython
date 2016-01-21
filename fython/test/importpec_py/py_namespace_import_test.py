s="""
.a.fy
	import numpy

	int x = |numpy.pi|


	print 'in b {:x}'

"""

from fython.test import *

shell('rm -rf a/ a.*') 

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
