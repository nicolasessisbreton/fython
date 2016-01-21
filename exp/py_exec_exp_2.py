import inspect
class A:
	def f(s, x):
		return x

a=A()

print(
	eval('f(1)', getmembers(a))
)