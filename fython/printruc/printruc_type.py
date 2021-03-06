from ..config import *

class PrintRuc(Buffer):
	def __init__(s, linecod):
		Buffer.__init__(s)
		
		s.linecod = linecod

		s.path = ''
		
		s.mode = 'a'

		s.unit = '*'

		s.advance = ''

		s.iostat = ''

		s.fmt = '*'		
		
	def throw(s, error, **kwargs):
		s.linecod.throw(error, **kwargs)