s = """
.a.fy
	class A:
		def pset f:
			self in
			int in x
			print '{:x}'

	A a
	a.f = 10
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
