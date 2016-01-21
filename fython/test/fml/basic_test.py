from numpy.testing import *
from fython.fml import *

class module:
	def __getattr__(s, n):
		return 0

m = module()	
m.verbose = m

x = ''
fa = fml(m, x)
print(repr(fa))
assert_equal(fa, '')

x = 'abc{:x}def'
f, a = fml(m, x).split(' = ')
print(f, '', a)
assert_equal(f, 'format("(","a,","g0,","a",")")')
assert_equal(a, "args('abc',x,'def')")

x = '{v:x}'
f, a = fml(m, x).split(' = ')
print(f, '', a)
assert_equal(f, 'format("(","a,",trim(<fytbk_int_to_char>(size(x))),"(g0,:,",achar(34),", ",achar(34),"),","a",")")')
assert_equal(a, "args('[',x,']')")

x = '{vc:x[:,i]}'
f, a = fml(m, x).split(' = ')
print(f, '', a)
assert_equal(f, 'format("(",trim(<fytbk_int_to_char>(size(x[:,i]))),"(g0,:,",achar(34),", ",achar(34),")",")")')
assert_equal(a, "args(x[:,i])")

x = 'in a {:x}'
f, a = fml(m, x).split(' = ')
print(f, '', a)
assert_equal(f, 'format("(","a,","g0",")")') 
assert_equal(a, "args('in a ',x)")


