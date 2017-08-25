Callback
----------

In Fython, it is possible to call a Python function.
Such callable function are called callback.
The trick is to pass the address of the callback.
This address is a simple integer, so, in fython, we cast it to a function pointer.

The code below shows how to transfer integer, real and arrays of these two.

The Fython code goes as follows.

.. code-block:: fython

  import:
    iso_c_binding(*)

  interface:
    def iso(c) py_fct:
      int(c_int) in:
        xint
      real(c_float) in:
        xreal
      int(c_int) in:
        nintv
        nrealv
      int(c_int) in:
        xintv(*)
      real(c_float) in:
        xrealv(*)
        
  def f:
    int(8) in:
      py_fct_pointer_int
    c_funptr:
      py_fct_pointer
    proc(py_fct) pointer:
      pyf
    int:
      x
      xv(2)
    real:
      y
      yv(2)

    print 'fython start: {:py_fct_pointer_int}'
    py_fct_pointer = transfer(py_fct_pointer_int, py_fct_pointer)
    c_f_procpointer(py_fct_pointer, pyf)
    print 'pyf called'
    x = 1
    y = 0.5
    xv = 10
    yv = 5.5
    pyf(x, y, 2, 2, xv, yv)
    print 'fython: after call: {:x} {:y} {v:xv} {v:yv}'
    print 'fython exit'
    
     
The Python goes like this

.. code-block:: python

  #>>>
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