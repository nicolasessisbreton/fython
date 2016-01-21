from fython import *

m = load('.variance')

# cube mean
print('calling variance')
x = Real(value=1)
y = Real(value=2)
z = Real(value=3)
r = Real()

m.variance(x, y, z, r)

print(' result in python', r[:])