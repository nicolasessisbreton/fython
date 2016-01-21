from ..config import *
from fython.kompile import *

def load(
	url,
	release = 0,
	force = 0,
	verbose = 0,
	run_main = 1,
):	
	fyfc.assert_compiler_setted
	
	cwd = get_frame_dir(1)

	m = kompile(
		url = url,
		cwd = cwd,
		release = release,
		force = force,
		verbose = verbose,
	)

	return m.get_wrapper(run_main)

	