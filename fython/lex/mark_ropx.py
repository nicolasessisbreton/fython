from ..config import *
from ..lexem import *

follower = [l.commax, l.rparx, l.rketx]

def mark_ropx(module):
	lexem = module.lexem

	for i in range(1, len(lexem)):

		x = lexem[i]
		t = x.type
		v = x.value.value

		if t == l.opx:
			if v == ':':
				n = lexem[i+1].type

				if n in follower:
					x.type = l.ropx
					x.value = v
					x.value = ROpX(x)
