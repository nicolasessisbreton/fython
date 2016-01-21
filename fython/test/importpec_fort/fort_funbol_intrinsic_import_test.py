s="""
.a.fy
	import iso_c_binding(c_float, c_int)

.b.fy
	import ifport(signalqq=signal)

.c.fy
	import iso_c_binding(*)

"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())

w = load('.b', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())

w = load('.c', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())

