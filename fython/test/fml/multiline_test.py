from fython.test import *
from fython.fml import *

class module:
	def __getattr__(s, n):
		return 0

m = module()	
m.verbose = m

x = '''
	{f:float} 
	{i:int} 
	{v:vector} 
	{vc:list_vector_inside}
	{a:string}
'''
x = trim(x)

fa = fml(m, x)
print(fa)
f, a = fa.split(' = ')
assert_equal(f, 'format("(","f,","a,","a,","i,","a,","a,","a,",trim(fytbk_int_to_char(size(vector))),"(g0,:,",achar(34),", ",achar(34),"),","a,","a,","a,",trim(fytbk_int_to_char(size(list_vector_inside))),"(g0,:,",achar(34),", ",achar(34),"),","a,","a",")")')
assert_equal(a, "args(float,' ',char(10),int,' ',char(10),'[',vector,']',' ',char(10),list_vector_inside,char(10),string)") 