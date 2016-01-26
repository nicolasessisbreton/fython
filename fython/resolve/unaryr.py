from ..config import *

def unaryR(linecod):
	s = linecod.modifier[0] # element

	if s.is_namex:
		if s.value in instruction:
			return instruction[s.value]

		else:
			return l.elementruc
	else:
		return l.elementruc

instruction = {
	l.breakk : l.breakruc,
	l.continuek : l.continueruc,
	l.passk : l.passruc,
	l.stop : l.stopruc,
}