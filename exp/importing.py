import sys

class Test(object):
	PATH_TRIGGER = 'fython'

	def __init__(s, path):
		print(0, path)
		if path != s.PATH_TRIGGER:
			print(1, path)
			raise ImportError()

	def find_module(self, fullname, path=None):
		print(11, fullname, 22, path)

sys.path_hooks.append(Test)

sys.path.insert(0, Test.PATH_TRIGGER)

import fython.a.b


"""
system is

import fython.work.module

use a 
	meta_path hook

collision with fython internal is guarded by the structure
	fython.sys

use ctypes to call binary
	carefull extract all interface code
		in separate facade module
"""