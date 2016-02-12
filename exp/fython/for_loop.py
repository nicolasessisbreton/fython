s="""
.a.fy
	int x

	if 1>2:
		x = 1
	elif 1>2:
		x = 1
		
	elif 1>2:
		x = 1

"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', force=1, release=0, verbose=0, run_main=0)
print(open(w.module.url.fortran_path, 'r').read())
