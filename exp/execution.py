class A:
	x = 1
	def run(s, c):
		print(eval(c, {}, A.__dict__))

	def g(s, t):
		return 2*t

a = A()

f = getattr(a, 'g')

print( eval('f(2)') )