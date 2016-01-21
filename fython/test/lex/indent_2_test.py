s = """
.a.fy
	real: # indent start
		x # continued

	#was skip previously
"""

from fython.test import *
shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', force=1, release=1, verbose=0)
print(open(w.module.url.fortran_path, 'r').read())
