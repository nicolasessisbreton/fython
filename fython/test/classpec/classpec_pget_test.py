s = """
.a.fy
	class A:
		def pget f:
			self in
			print '1'

	A a
	a.f
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
