from fython import *

m = load('.mean')

# accessing a global variable
p = m.plank()

# setting a global variable
p[:] = 6

# cube mean
print('cube mean')
x = Real(value=1)
y = Real(value=2)
z = Real(value=3)
r = Real()

m.cube_mean(x, y, z, r)

print(' result in python', r[:])

# moving mean
print('\nmoving mean 1')

n = Int(value=5)
x = Real(value=[1, 2, 3, 4, 5])
m.moving_mean(n, x)

print('  result in python', x[:])

# an other time
print('\nmoving mean 2')
x[0] = 10
x[1] = 20
m.moving_mean(n, x)

print('  result in python', x[:])

# string mean
x = Char(size=3, value=['abc', 'xyz', 'ijk'])
m.string_mean(x, r)

print('string mean', r[:])