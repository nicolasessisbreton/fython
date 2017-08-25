import:
  iso_c_binding(*)

interface:
  def iso(c) py_fct:
    int(c_int) inout:
      xint
    real(c_float) inout:
      xreal
    int(c_int) in:
      nintv
      nrealv
    int(c_int) inout:
      xintv(*)
    real(c_float) inout:
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
  