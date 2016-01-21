s = """
.a.fy
	integer: 
		a=1 
		b=1 
		c=1 
		n=1 
		m=1
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)

# print(open(w.module.url.fortran_path, 'r').read())

