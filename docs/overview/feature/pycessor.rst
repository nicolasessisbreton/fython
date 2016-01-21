Pycessor
~~~~~~~~

Use Python to easily do your preprocessing magic

.. code-block:: fython

  import numpy

  real pi = |numpy.pi|

  # lazy initialization of exotic random variate
  real v(1e3)

  |
    for i in range(1000):
      write('v[i] = {:f}'.format(numpy.random.uniform()))

  |

Any expression enclosed in bars is evaluated against the imported Python module.
The return value of a pycession can be any valid Fython code.