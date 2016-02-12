from ..config import *
from ..lexem import *

preceder = [
	l.semix, 
	l.commax, 
	l.lpcax, 
	l.lkcax, 
	l.lparx, 
	l.lketx, 
	l.funx, 
	l.slicex,
]

follower = [l.commax, l.rparx, l.rketx]

def mark_eopx(module):
	lexem = module.lexem

	for i in range(1, len(lexem)):

		x = lexem[i]
		t = x.type
		v = x.value.value

		if t == l.opx:
			if v in [':', '*']:
				p = lexem[i-1].type
				n = lexem[i+1].type

				if p in preceder and n in follower:
					x.type = l.eopx
					x.value = v
					x.value = EOpX(x)