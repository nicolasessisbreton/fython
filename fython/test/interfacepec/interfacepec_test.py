s = """
.a.fy
	interface:
		def f:
			real in x

	interface abstract:
		def g:
			int arg y
			real dimension(:) pointer inout z
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
print(open(w.module.url.fortran_path, 'r').read())
