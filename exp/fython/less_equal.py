s="""
.a.fy
	if 1 >= 2:
		print '1'
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
