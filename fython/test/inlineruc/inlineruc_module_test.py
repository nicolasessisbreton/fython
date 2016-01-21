s="""
.a.fy
	def f:
		print '1'

	def ff:
		print '2'

.b.fy
	import .a = a

	inline: a.f a.ff
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.b', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())