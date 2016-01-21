from fython.unit import *

class SliceX(Unit):
	unit = l.slicex

	def __str__(s):
		if s.guid_overwrite:
			return s.guid_overwrite

		else:
			return s.module.get_guid_tag(s.value)

