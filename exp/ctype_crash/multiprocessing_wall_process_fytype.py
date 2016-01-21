from multiprocessing import *
from ctypes import *
from fython.fytypes import *

x = Real(value=1)

print(x[:])

def f():
	print(1)
	print(x[:])
	x[:] *= 10
	print(x[:])
	print(2)

if __name__ == '__main__':
	p = Process(target=f)
	p.start()
	p.join()
	print(3, x[:], p.exitcode)
