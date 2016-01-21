# from dill import *
from pickle import *

class A:
	@property
	def x(s):
		return 1

a = A()
a.q = A()
print(a.x)

print(
	
dumps(a, protocol=0)

)