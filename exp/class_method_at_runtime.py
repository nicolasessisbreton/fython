class A:
	pass

	def f(s, x):
		s.g(s, x)

def g(s, x):
	print(type(s))
	print(1, x)

a = A()

a.g = g

a.x = g
a.f(3)

a.x(1, 5)