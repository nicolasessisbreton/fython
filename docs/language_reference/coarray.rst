Coarray
---------

A coarray is defined by specifying its codimension in bracket

.. code-block:: fython

  real x[*]
  real y(10)[*]

A coarray is accessed with the slice notation

.. code-block:: fython

 x = 1 # this_image() x
 x[2] = 2 # x on image 2

 y[1] = 1 # this_image() y
 y[:][2] = 1 # y on image 2

To use coarray in Fython, you need to set the compiler to use with the
``set_compiler`` function

.. code-block:: python

  #>>>
  from fython import *

  set_compiler(
    cmd = 'ifort',
    prefix = '',
    infix = '_mp_',
    suffix = '_',
    debug = '-coarray -coarray-num-images=5',
    release = '-coarray -coarray-num-images=5',
    error_regex = 'error:',
  )

  m = load('.coarray_test')



