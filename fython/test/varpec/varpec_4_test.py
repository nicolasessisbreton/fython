s = r"""
.a.fy
	char(10): variable_name='./file', string = 'abcdef'
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
print(open(w.module.url.fortran_path, 'r').read())
