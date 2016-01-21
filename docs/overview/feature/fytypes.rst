**FyTypes**

You can send Python object by reference to Fython
using the intuitive fytypes

.. code-block:: python
  
  from fython import *

  m = load('stat.mean')  

  nb_element = Int(value=3)
  x = Real(value=[1, 2, 3])
  result = Real()

  m.mean(nb_element, x, result)

  print(result[:])

When using a fytype, you always access or modify its value with a slice.
Wheter the value is a scalar or an array.

.. code-block:: python

  x[:2] += 10

  result[:] *= 10  

Changes made by Fython are propagated back to Python

.. code-block:: python
  
  m.moving_average_in_place(x)

  print('moving average is:', x[:])  

You can also access and modify global Fython variables

.. code-block:: python

  n = m.roundoff_tolerance()
  n[:] = 1e-5

All the above works for real, integer and string variables of any dimension

.. code-block:: python

  cities = Char(size=30, value=['montreal', 'tokyo', 'santiago'])
  result = Char(size=30)

  m.word_mean(nb_element, cities, result)

