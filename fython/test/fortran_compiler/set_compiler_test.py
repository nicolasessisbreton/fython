s="""
.a.fy
	import iso_c_binding(*)
	print '1'
"""

from fython.test import *

set_compiler(
	cmd = 'ifort',
	prefix = '',
	infix = '_mp_',
	suffix = '_',
	debug = '',
	release = '',
	link = '',
	error_regex = 'error:',
	warning_regex = 'warnings:'
)

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)

use_ifort() # back to ifort