s="""
.a.fy
	class A:
		real x
		def g:
			print '1'

	def f:
		inline A.g
		
	f()
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
