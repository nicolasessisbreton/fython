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
      int(c_int) value in:
        xint
      real(c_float) value in:
        xreal
      int(c_int) value in:
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
    print 'fython exit'
    
The Python goes like this

.. code-block:: python

  #>>>
  from mttc import *
  from ctypes import *
  import numpy as np

  m = load('.pycall', force = 2)

  def f(xint, xreal, nintv, nrealv, xintv, xrealv):
    array_type = c_int*nintv
    addr = addressof(xintv.contents)
    xintv = np.array(array_type.from_address(addr), copy=0)

    array_type = c_float*nrealv
    addr = addressof(xrealv.contents)
    xrealv = np.array(array_type.from_address(addr), copy=0)

    print('hello from python', xint, xreal, nintv, nrealv, xintv, xrealv)

  c_fun_dec = CFUNCTYPE(None, c_int, c_float, c_int, c_int, POINTER(c_int), POINTER(c_float))

  c_fun = c_fun_dec(f)

  c_fun_int = cast(c_fun, c_void_p).value

  m.f(
    py_fct_pointer_int = Int8(c_fun_int),
  )

