Syntax
-------

In Fython a statement is formed by a keyword, modifiers and target

.. code-block:: shell

  keyword modifier* target

The keyword is the action performed by the statement.
The modifiers mutate the default behavior of the actions,
The action dictated by the keyword and modifiers is then
applied to all the target.

.. code-block:: fython

  real pointer x

  real pointer: x y z
  real pointer: x, y, z

  real pointer:
    x
    y
    x

  real pointer:
    x, y, z
    a, b, c

The comma is necessary for target that are non atomic

.. code-block:: fython

  real cons: x=1, y=2, z=3

The only exception to the statement construction
are in-place assignment operation

.. code-block:: fython

  real: x y

  x = y + 1
  x += 10

Modifiers are also called attributes.

Any modifier that is allowed in Fortran can also be used in Fython

.. code-block:: fython

  real pointer x
  int allocatable contiguous y

Arrays are defined by indicating their dimensions

  .. code-block:: fython
  
    real:
      x(10)
      y(1:10, 0:5)

Array elements are accessed with the slice notation

.. code-block:: fython

  x[1:6] => y[2, :]

You can initialize an array or use an array in place with the bracket notation

.. code-block:: fython

  real x(3) = [1, 2, 3]

  f([1, 2, 3])
