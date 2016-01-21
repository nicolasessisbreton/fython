import os
import inspect

def get_frame_dir(level=0):
	level += 1
	r = os.path.dirname(
		os.path.abspath(
			inspect.getfile(
				inspect.stack()[level][0]
			)
		)
	)
	
	return r