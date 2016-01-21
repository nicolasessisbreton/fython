from importlib import import_module
from fython.config import *

def imp(url):
	url = Url(
		url = url,
		cwd = get_frame_dir(1),
		ext = exts.py,
	)
	return import_module(url.dotted)