s = """
.a.fy
	def i:
		int in x
		int out z
		z = x*10

	def r:
		real in x
		real out z
		z = x*10

	def iv:
		int dimension(2) in x
		int dimension(2) out z
		z = x*10

	def rv:
		real dimension(2) in x
		real dimension(2) out z
		z = x*10
		
	def c:
		char(3) in x
		char(3) out z
		z = x

	def cv:
		char(3) dimension(2) in x
		char(3) dimension(2) out z
		z = x
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

m = load('.a', release=1, verbose=0, run_main=0)

x = Int()
z = Int()
x[:] = 1
m.i(x, z)
print(x[:], z[:])
assert_equal(z[:], 10)

x = Real()
z = Real()
x[:] = 1
m.r(x, z)
print(x[:], z[:])
assert_equal(z[:], 10)

x = Int(shape=[2])
z = Int(shape=[2])
x[:] = 1
m.iv(x, z)
print(x[:], z[:])
assert_equal(z[:], [10, 10])

x = Real(shape=[2])
z = Real(shape=[2])
x[:] = 1
m.rv(x, z)
print(x[:], z[:])
assert_equal(z[:], [10, 10])

x = Char(size=3)
z = Char(size=3)
x[:] = 'xyz'
m.c(x, z)
print(x[:], z[:])
assert_equal(z[:], b'xyz')

x = Char(size=3, shape=[2])
z = Char(size=3, shape=[2])
x[:] = 'xyz'
m.cv(x, z)
print(x[:], z[:])
assert_equal(z[:], [b'xyz', b'xyz'])







