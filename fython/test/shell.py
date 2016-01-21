from ..config import *
from os import system

def shell(cmd):
	cwd = get_frame_dir(1)	
	cmd = 'cd {:s} && {:s}'.format(cwd, cmd)
	system(cmd)