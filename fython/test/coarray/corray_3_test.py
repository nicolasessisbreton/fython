s = """
.a.fy
	int i
	int a[*]

	if this_image() == 1:
		for i in [1, num_images()]:
			a[i] = i

	sync all
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

# w = load('.a', release=1, verbose=0, run_main=1)
# print(open(w.module.url.fortran_path, 'r').read())
