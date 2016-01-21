from fython.unit import *

class FunX(Unit):
	unit = l.funx

	def __str__(s):
		if s.guid_overwrite:
			return s.guid_overwrite
			
		else:
			return s.module.get_guid_tag(s.value)

