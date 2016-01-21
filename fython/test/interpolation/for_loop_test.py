s="""
.a.fy
	|
		for i in [1, 2]:
			write("print '{:d}'", i)
	|
"""

from fython.test import *

shell('rm -rf a/ a.* b.*') 

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
