s="""
.a.fy
	def f:
		print '1'

.b.fy
	import .a(*)

	def g:
		inline f

	g()
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.b', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
