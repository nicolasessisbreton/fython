s = """
.a.fy
	def f:
		T in x
		T res r
		r = x * 10
		
.b.fy
	import .a(*)
	|| T=real ||

	print '{:f(10.)}'
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.b', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
