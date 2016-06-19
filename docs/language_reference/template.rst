Template
---------

A function template is defined with the ``def`` statement

.. code-block:: python

  def f:
    T in x
    T res r
    r += x

  def g = f(T=real)

To templatize a whole package use the import statement

.. code-block:: fython

  import quicksort(*)
  ||type_provide=stat.mean, target_class=KMean||

Package interpolation can also be multilines

.. code-block:: fython

  import quicksort(*)
  ||
    type_provide = stat.mean
    target_class = KMean

  ||

To disable package interpolation during a package import,
use the ``asis`` modifier. 

.. code-block:: fython

  import asis random

This is usefull to avoid further interpolation during an ongoing package interpolation.
