from types import ModuleType

m = ModuleType('interpolant')

m.x = 1
m.y = lambda : 1

print(m.x, m.y())

exec('from numpy import *', m.__dict__)

print(m.array([1,2]))

print(eval('x + y() + array([1,2])',m.__dict__))