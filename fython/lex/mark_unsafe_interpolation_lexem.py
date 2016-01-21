from ..config import *

def mark_unsafe_interpolation_lexem(module):
	lexem = module.lexem
	n = len(lexem)
	group = 0

	for i in range(n):
		x = lexem[i]

		if x.type in [l.lpackagex, l.funx]:
			group += 1

		elif x.type in [l.rpackagex, l.rparx]:
			group -= 1

		elif group:
			if x.value.value == '=':
				p = lexem[i-1].value
				p.is_interpolation_safe = 0

	# for import statement this is the contrary : safe = unsafe
	importk = 0
	wait_for_dedent = 0
	for i in range(n):
		x = lexem[i]

		if x.value.value == l.importk:
			importk = 1

		elif x.type == l.indentx:
			if importk:
				wait_for_dedent = 1

		elif x.type == l.newlinex:
			if not wait_for_dedent:
				importk = 0

		elif x.type == l.dedentx:
			if wait_for_dedent:
				wait_for_dedent = 0
				importk = 0

		elif importk:
			if x.value.value == '=':
				safe = lexem[i-1].value
				unsafe = lexem[i+1].value
				safe.is_interpolation_safe = 1
				unsafe.is_interpolation_safe = 0