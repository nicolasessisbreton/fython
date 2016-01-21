from pickle import load
from ..config import *
from .fymodule import FyModule
from .fortmodule import FortModule
from .somodule import SoModule

def get_module(url, stack):
	if url.ext in exts.fy:
		m = FyModule()
		m.get_and_parse(url, stack)

	elif url.ext in exts.fort:
		m = FortModule(url, stack)

	else:
		m = SoModule(url)

	return m