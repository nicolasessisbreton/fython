Operator
--------

Fython has the augmented assignment operators,
the logical operator, the bitwise operators,
and the pointer operator.

.. code-block:: fython

  x += 1
  x -= 1
  x *= 2
  x /= 2

  x <<= 1
  x &= 1
  x ^= 1
  x |= 1
  x >>= 1


  x < <= == != => > y # this is an invalid syntax 
  
  x and y or b not c

  x >> 1 + y << 4

  x => y # pointer

The min and max operator are often convenient.

.. code-block:: fython

  x ++= y # x = max(x, y)
  x --= y # x = min(x, y)