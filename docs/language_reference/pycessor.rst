Pycessor
--------

Pycession instruction are specified within bars.
The Python imports necessary for the pycession at the top of your Fython module

.. code-block:: python

  import numpy = np

  pi = |np.py|

A pycession can be multiline

.. code-block:: fython

  |
    for T in ['real', 'int']:
      write('def f_{T:s} = g(T = {T:s})'.format(T)
  |

The signature of the ``write`` function is

.. code-block:: python

  #>>>
  write(
    string,
    *args,
    end = '\n',
    **kwargs,
  )

The positional and keyword arguments are used to format the ``string`` argument.

When a pycession is a Python expression, its value is directly inserted
in your Fython code.
The ``write`` function is necessary when the pycession is not an expression.
Each string passed to the ``write`` function is inserted in your Fython code.
The ``end`` argument is appended to the string.

Any valid Python code is possible in a Pycession.

The Pycessor is a preprocessor.
Do not use it to pass arguments to Fython
because the dependency system will not see any post-compilation change in your Python module.
The Pycessor is meant to facilitate the generation of tedious code,
or to trigger any kind of necessary preparation before compilation.