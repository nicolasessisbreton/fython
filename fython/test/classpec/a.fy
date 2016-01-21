int z

class A:
	real x

	def pure f:
		self in
		real res r
		r = self.x + z

	def pget h:
		s arg
		real res r
		r = 10 + s.x

	def g:
		s inout
		real in x
		real res r
		r = x + 3 + s.h


A a
z = 1
a.x = 1
print '{:a.f() + a.g(1.) + a.h}'