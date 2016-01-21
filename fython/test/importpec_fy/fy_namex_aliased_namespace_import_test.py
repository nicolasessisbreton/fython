s="""
.temp_package.__init__.fy
	int x = 10
	print 'in a {:x}'

.b.fy
	import temp_package 

	int x = 1

	print 'in b {:x} {:temp_package.x}'

"""
from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

import sys
sys.path.append(get_frame_dir())

w = load('.b', force=1, release=1, verbose=0, run_main=0)
print(open(w.module.url.fortran_path, 'r').read())

sys.path.pop(0)
