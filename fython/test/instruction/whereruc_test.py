s = """
.a.fy
	int x(10)
	
	where x >1:
		x += 1
	elwhere x < 0 :
		x-= 1
	else:
		x **= 8

"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
