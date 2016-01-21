class A:
	real x
	def g:
		print '1'

class B:	
	inline A

B b
b.g()