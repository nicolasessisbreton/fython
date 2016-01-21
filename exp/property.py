class A:
	def f(s):
		return 9
	x = property(f)


a = A()

print(a.x)


@property
def x():
	return a

print(x)