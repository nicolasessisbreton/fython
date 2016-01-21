from pickle import load
from ..config import *
from .fortmodule import FortModule
from .somodule import SoModule

def restore_module(url, stack):
	if url.ext in exts.fy:
		m = load(open(url.pickle, 'rb')) 

	elif url.ext in exts.fort:
		m = FortModule(url)

	else:
		m = SoModule(url)

	m.stack = stack
	m.release = stack.release
	m.debug = stack.debug
	m.verbose = stack.verbose
	
	return m