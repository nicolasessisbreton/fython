Fython is Fortran with a Python syntax.
If performance requirements
periodically forces you out of Python,
with Fython you won't feel it

**hello.fy**

.. code-block:: fython

  real offset = 0
  
  def fast_sum:
    real in v(1e9)
    real res r

    r = 0
    for i in [1, 1e9]:
      r += v[i] + offset

    print('The sum is {:sum(v)}')

The loop above is automatically parallelized
by the Fortran compiler that powers Fython.

Usage in Python is as simple as

**hello.py**

.. code-block:: python

  import fython
  import numpy as np

  hello = fython.load('.hello')

  offset = hello.offset()
  v = fython.Real(shape=[1e9])

  offset = 10
  v[:] = np.random.uniform(0, 1, 1e9)

  hello.fast_sum(v)