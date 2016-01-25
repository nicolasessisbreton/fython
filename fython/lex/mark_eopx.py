from ..config import *
from ..lexem import *

def mark_eopx(module):
	lexem = module.lexem

	for i in range(1, len(lexem)):
		p = lexem[i-1].type

		x = lexem[i]
		t = x.type
		v = x.value.value

		if t == l.opx:
			if v in [':', '*']:
				if p in [l.semix, l.commax, l.lpcax, l.lkcax, l.lparx, l.lketx]:
					x.type = l.eopx
					x.value = v
					x.value = EOpX(x)