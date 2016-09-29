s = r'''
.a.fy
	print """
			{:1}
			{:2}
			{:3}
	"""
'''

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=1)
# print(open(w.module.url.fortran_path, 'r').read())
