from ..config import *

class SourceModule(Data):
	def __init__(s, parent_module, source, line_offset):
		s.value = parent_module.value

		s.release = parent_module.release
		s.debug = parent_module.debug
		s.verbose = parent_module.verbose

		s.source = source
		s.source_lines = source.split('\n')
		s.line_offset = line_offset
