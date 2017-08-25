from mttc import *
from ctypes import *
import numpy as np

m = load('.fy_caller', force = 1)

@fycallback(Int, Real, Int, Int, Int, Real)
def f(xint, xreal, nintv, nrealv, xintv, xrealv):
  x = IntP(xint)
  y = RealP(xreal)
  xv = IntP(xintv, nintv)
  yv = RealP(xrealv, nrealv)

  print('hello from python', x, y, xv, yv)

  x[:] *= 2 
  y[:] *= 2
  xv[:] *= 2
  yv[:] *= 2


m.f(py_fct_pointer_int = f.fy_address)