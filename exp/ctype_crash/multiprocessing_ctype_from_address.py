from multiprocessing import *
from ctypes import *

x = c_int(1)
a = addressof(x)

print(x.value)

def f():
	print('a')
	x = cast(a, POINTER(c_int))
	x = x.contents
	print('b', x.value)
	x.value *= 10
	print(x.value)
	print('c')

if __name__ == '__main__':
	p = Process(target=f)
	p.start()
	p.join()
	print(3, x.value, p.exitcode)
