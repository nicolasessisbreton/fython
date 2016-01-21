from ..config import *

def defR(linecod):
	m = linecod.modifier[-1]

	if m.is_ibol:
		return l.lexiruc

	else:
		return l.routpec