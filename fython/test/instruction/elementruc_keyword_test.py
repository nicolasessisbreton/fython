s = """
.a.fy
	int i
	pass
	for i in [1, 2]:
		continue
		break
		
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
