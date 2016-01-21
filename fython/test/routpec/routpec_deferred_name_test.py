s = """
.a.fy
	print 'g {:g()}'

	def g:
		real res r
		r = 3 + f()

	def f:
		real res r
		r = 10

"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())

