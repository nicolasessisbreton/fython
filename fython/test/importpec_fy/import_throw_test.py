s="""
.a.fy
	int x_a = 10

.b.fy
	import:
		.aa(*)

"""

from fython.test import *

shell('rm -rf a/ a.* b.* c.*')

writer(s)

# w = load('.b', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
