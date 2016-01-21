from ..config import *
from ..lexem import *

def mark_opx_from_semix(module):
	lexem = module.lexem
	n = len(lexem)
	ndx =[]

	for i in range(n):
		x = lexem[i]
		t = x.type		

		if t == l.linefeedx:
			last_linefeedx = i
			semix_seen = 0

		elif t in [l.semix, l.colonx, l.lpackagex]:
			semix_seen = 1

		elif t == l.newlinex:
			if semix_seen:
				ndx.append([last_linefeedx, i])

	for a, b in ndx:
		for i in range(a, b):
			if lexem[i].type == l.iopx:
				lexem[i].type = l.opx
				lexem[i].value = '='
				lexem[i].value = OpX(lexem[i])