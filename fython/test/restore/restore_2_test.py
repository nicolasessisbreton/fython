s = """
.a.fy
	int z

"""

from fython.test import *
# shell('rm -rf a/ a.* b.*')
# writer(s)
w = load('.a', release=1, verbose=0, run_main=0)
print(open(w.module.url.fortran_path, 'r').read())

s = """
.b.fy
	import .a(*)

	print '{:z}'

"""

# writer(s)
w = load('.b', release=1, verbose=0, run_main=0)
print(open(w.module.url.fortran_path, 'r').read())

