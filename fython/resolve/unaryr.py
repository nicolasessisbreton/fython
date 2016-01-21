from ..config import *

def unaryR(linecod):
	s = linecod.modifier[0] # element

	if s.is_namex:
		if s.value == l.breakk:
			return l.breakruc

		elif s.value == l.continuek:
			return l.continueruc

		elif s.value == l.passk:
			return l.passruc

		else:
			return l.elementruc
	else:
		return l.elementruc
