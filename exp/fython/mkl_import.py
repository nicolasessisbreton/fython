s="""
.a.fy
	# |import sys; sys.path.append('/opt/intel')|

	# import sys # sys not in standard pythonpath ; not supported for the moment
	# |sys.path.append('/opt/intel')|

	import mkl.include.mkl_vsl(*)
	import mkl.lib.intel64.libmkl_intel_lp64(*)

"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
print(open(w.module.url.fortran_path, 'r').read())
