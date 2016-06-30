from fython.unit import *

class PackageBol(Unit):
	unit = l.packagebol
	
	def __init__(s, lpackagex):
		s.module = lpackagex.module
		s.lineno = lpackagex.lineno

		s.raw = []		
		s.lexem = []

		s.modifier = [lpackagex]
		s.args = []

		s ^ lpackagex

	# &: add modifier
	def __and__(s, other):
		s ^ other

		if other.is_semibol:
			s.modifier.extend(other.modifier)
			s.args.extend(other.modifier)

		elif not other.is_rpackagex:
			s.modifier.append(other)
			s.args.append(other)
			
		return s

	def clone(s, module):
		lpackagex = s.raw[0].clone(module)
		t = PackageBol(lpackagex)

		for m in s.raw[1:]:
			t & m.clone(module)	

		return t
		
	@property
	def hash(s):
		r = ''
		for x in s.lexem:
			r += x.value.value

		return md5(r)

	@property
	def interpolation(s):
		r = {}
		for a in s.args:
			x = a.modifier[0].pre_interpolation_value
			y = a.lexem[2:] # pop x=
			r[x] = y
		return r

