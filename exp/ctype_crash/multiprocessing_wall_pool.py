from multiprocessing import *
from ctypes import *

def f(x):
	print(1)
	string_at(1)
	print(2)

if __name__ == '__main__':
	p = Pool(1)
	p.apply(f, [0])
	print(3)