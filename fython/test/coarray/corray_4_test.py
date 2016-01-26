s = """
.a.fy
	int a[*]

	critical:
		a = 1

	stop
	error stop
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

# w = load('.a', release=1, verbose=0, run_main=1)
# print(open(w.module.url.fortran_path, 'r').read())
