s="""
.a.py
	x = 10

.b.fy
	import .a = c

	int x = |c.x|


	print 'in b {:x}'

"""

from fython.test import *

shell('rm -rf a/ a.* b.*') 

writer(s)

w = load('.b', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
