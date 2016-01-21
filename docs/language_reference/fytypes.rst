FyTypes
----------

Only three kinds of data type can travel back and forth
between Python and Fython

.. code-block:: python

  #>>>
  from fython import *
  x = Real()
  y = Int()
  z = Char(size=100)

  m = load('.mean')

  m.f(x, y, z)

Only function that have no return value can be called from Python.
In Fortran term, ``f`` must be a subroutine.

Fython can modify in-place the element send by Python.
The change will be seen in Python.
The same is true in Python.
In change made to a fytype in Python, will be seen in Fython.

The value of a fytype is always accesses with a slice, wheter the fytype is a scalar 
or a vector

.. code-block:: python

  #>>>
  x = Real()
  y = Real(value=[1, 2, 3])

  x[:] = 9
  y[:1] = 10 + x[:]

The three Fytypes all have the optional arguments ``size``, ``shape`` and ``value.
They are shown below with their default value

.. code-block:: fython

  #>>>
  x = Real(size=4, shape=[], value=None)
  y = Int(size=4, shape=[], value=None)
  z = Char(size=100, shape=[], value=None)

An empty list indicates a scalar.
A vector is defined by specifying the number of element in each dimension.

.. code-block:: python

  #>>>
  x = Real(shape=[10, 10])

The argument ``value`` is used to connect a fytype to a Python object.
Any change made to the fytype will be reflected in the Python object

.. code-block:: python

  #>>>
  x = [1, 2, 3]
  y = Real(value=x)

To access a global variable, use its name

.. code-block:: python

 #>>> 
  from fython import *
  m = load('.mean')
  tolerance = m.tolerance()

Fython will automatically detects the type of the variable and use the default fytype initializer above.
You can specify the variable specification yourself

.. code-block:: python

  #>>>
  x = m.x(size=8, shape=[10])

Once setted the shape of fytype cannot change.
This limitation can be overcome by letting Python and Fython share informations

.. code-block:: python

  #>>>
  m = load('.mean')
  m.compute()
  n = m.result_size()
  result = m.result(size=n[:])


