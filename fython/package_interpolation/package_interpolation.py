from ..config import *

class Package_Interpolation(Data):
	def __init__(s):
		s.frame = [{}] # most recent last
		s.hash_stack = []
		s.pickle_hash_tag = ''
		s.is_asis_import = 0

	def set_asis_import(s):
		s.is_asis_import = 1

	def unset_asis_import(s):
		s.is_asis_import = 0

	def add_lexiruc_interpolation(s, interpolation):
		s.frame.append(interpolation)

	def add(s, packagebol):
		
		s.frame.append(packagebol.interpolation)

		s.hash_stack.append(packagebol.hash)
		s.pickle_hash_tag = s.get_hash()

	def pop_lexiruc_interpolation(s):
		s.frame.pop()
		
	def pop(s):
		s.frame.pop()

		s.hash_stack.pop()
		s.pickle_hash_tag = s.get_hash()
	
	def get_hash(s):
		if s.hash_stack:
			return '.' + str(hash(''.join(s.hash_stack)))
			
		else:
			return ''
	
	def __contains__(s, name):
		return name in s.frame[-1]

	def __getitem__(s, name):
		return s.frame[-1][name]


	@property
	def pickle_hash(s):
		if s.is_asis_import:
			return ''
		else:
			return s.pickle_hash_tag