from ..config import *

class Package_Interpolation(Data):
	def __init__(s):
		s.frame = [{}] # most recent last

	def add(s, interpolation):
		s.frame.append(interpolation)

	def pop(s):
		s.frame.pop()
		
	def __contains__(s, name):
		return name in s.frame[-1]

	def __getitem__(s, name):
		return s.frame[-1][name]