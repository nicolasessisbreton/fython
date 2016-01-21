s = """
.a.fy
	int i
	real: x(10) y(10, 10)

	if x[1]>1:
		x[2:1] = x[2:1] + y[2:1,6]
		for i in [1, 2]:
			print '2'
	print '''
	a
	'''

	print 'a'

	print "b"

"""

from fython.test import *
shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
