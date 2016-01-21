from inspect import isfunction, ismethod, getmembers
import math

try:
	a

except Exception as e:
	print(e, repr(e))

class A:
	def __init__(s, a):
		s.a = a

	def __hash__(s):
		return hash(s.a)

	def __eq__(s, other):
		return s.a == other.a

	def __str__(s):
		return 'aa'

	def __format__(s, fmt):
		return 'aa'

	def x(s):
		print('x')

	def f_x(s, t):
		print('x', t)

a = A(1)

print(a.__class__.__name__)
print(hasattr(a, '__str__'))

print(a)
print('{:s}'.format(a))
dd
# b = A(2)
# print(a==b)
# print(set([a,a]))
# print(set([a,b]))

# print(
# 	isfunction(a.x),
# 	ismethod(a.x),
# )

# getattr(a, 'x')()

# for n, f in getmembers(a):
# 	if n.startswith('f_'):
# 		print(11, f(22))

for n, f in getmembers(a):
	if isfunction(f) or ismethod(f):
		print(1, n, f)
	else:
		print(2, n, f)