s = """
.a.fy
	int i = 1
	int dimension(2) iv = [1, 2]

	real r = 1
	real dimension(2) rv = [1, 2]

	char(3) c = 'abc'
	char(3) dimension(2) cv = ['abc', 'def']
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)

m = load('.a', release=1, verbose=0, run_main=0)

# print('**retrieved')
r = m.r()
rv = m.rv(4, [2])

i = m.i()
iv = m.iv(4, [2])

c = m.c(3)
cv = m.cv(3, [2])

# print(r)
# print(rv)
# print(i)
# print(iv)
# print(c)
# print(cv)

# print('**changed')
r[:] = 10
rv[:] *= 10
i[:] = 10
iv[:] *= 10
c[:] = 'xyz'
cv[:] = 'xyz'

# print(r[:], rv[:])
# print(i[:], iv[:])
# print(c[:], cv[:])

# print('**reloaded')
r = m.r()
rv = m.rv(4, [2])

i = m.i()
iv = m.iv(4, [2])

c = m.c(3)
cv = m.cv(3, [2])

# print(r[:], rv[:])
# print(i[:], iv[:])
# print(c[:], cv[:])

# assertion
assert_equal(r[:], 10)
assert_equal(rv[:], [10, 20])

assert_equal(i[:], 10)
assert_equal(iv[:], [10, 20])

assert_equal(c[:], b'xyz')
assert_equal(cv[:], [b'xyz', b'xyz'])
