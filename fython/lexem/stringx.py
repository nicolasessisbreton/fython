from fython.unit import *

tab = "'//char(9)//'"
newline = "'//char(10)//'"

class StringX(Unit):
	unit = l.stringx

	def __str__(s):
		r = s.value

		r = "'{:s}'".format(r)
			
		r = r.replace('\t', tab)
		r = r.replace('\n', newline)
		
		return r
