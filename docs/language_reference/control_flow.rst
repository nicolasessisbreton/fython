Control Flow
------------

Fython has ``if``, ``for``, ``fop``, ``while`` and ``where`` statement

.. code-block:: fython

  if x < 1:
    y += 1

  elif x < 1:
    y += 2

  else:
    y = 0

The third argument in the bracket of a ``for`` statement is the step size

.. code-block:: fython

  for i in [1, 2]:
    r += x[i]

  for i in [0, 10, 2]:
    r += x[i] # 0, 2, 4, ...

The ``fop`` loop is a parallel for loop. The Fortran equivalent is a do concurrent loop.

.. code-block:: fython

  fop i in [1, 2]:
    r += x[i]

The while loop is

.. code-block:: fython

  while x < 10:
    x += 1

The where statement is

.. code-block:: fython

  where x > 1:
    x = y

  elwhere x < 1:
    x -= 1

  else:
    x = 0
