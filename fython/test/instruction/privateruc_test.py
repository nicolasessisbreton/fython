s = """
.a.fy
	integer: x y z a b c d

	private x
	private: y z

	private:
		a
		b
		c, d
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0)
# print(open(w.module.url.fortran_path, 'r').read())
