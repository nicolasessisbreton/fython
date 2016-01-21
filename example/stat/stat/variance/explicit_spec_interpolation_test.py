from fython import *

m = load('.explicit_spec_interpolation')

print('calling f')
x = Real(value=1)
y = Real()
m.f(x, y)

print(' result in python', y[:])

print('calling g')
x = Real(value=1)
y = Real()
m.g(x, y)

print(' result in python', y[:])