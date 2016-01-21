from ..config import *

class SoModule(Data):
	is_fymodule = 0
	is_fortmodule = 0
	is_somodule = 1
	dependency = []	
	guid ={}
	
	def __init__(s, url):
		s.url = url
		s.value = url.dotted

	def resolve(s):
		pass		

	def save(s):
		pass
		
	def write_fortran(s):
		pass	

	def compile_fortran(s):
		pass