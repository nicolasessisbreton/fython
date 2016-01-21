s = """
.a.fy
	class temp A:
		T x

		def pget f:
			s in
			U res r	
			r = s.x * scale

	def G = A(
		T = real,
		U = int,
	)

	G g	
	g.x = 10
	print '{:g.f}'

"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', release=1, verbose=0, run_main=0)
print(open(w.module.url.fortran_path, 'r').read())
