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

def mark_uopx(module):
	lexem = module.lexem

	for i in range(1, len(lexem)):

		x = lexem[i]
		t = x.type
		v = x.value.value

		if t == l.opx:
			if v in ['-', '+', ':']:
				p = lexem[i-1].type

				if p in preceder:
					x.type = l.uopx
					x.value = v
					x.value = UOpX(x)
