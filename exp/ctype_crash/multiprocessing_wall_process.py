from multiprocessing import *
from ctypes import *

def f():
	print(1)
	# string_at(1)
	print(2)

if __name__ == '__main__':
	p = Process(target=f)
	p.start()
	p.join()
	print(3, p.exitcode)
	