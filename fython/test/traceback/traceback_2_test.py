s = """
.a.fy
	def boom:
		real x
		subboom(x)	

	def subboom:
		real inout x
		x = 1 / 0
"""
from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', force=1, release=0, verbose=0, run_main=1)

w.verbose()

try:
	w.boom()
except Exception as e:
	print(e)
	assert 'sigfpe' in str(e)


