__version__ = '1.0'

from fython.load import *
from fython.fytypes import *
from fython.hello import *
from fython.config import set_compiler, find_compiler, use_ifort, use_gfortran, use_mkl
from fython.test.writer import writer 

find_compiler()