Template
~~~~~~~~

Overload of a function or a class can be created with template interpolation

.. code-block:: fython

  def temp f:
    T in x
    T res r
    r = x + 10

  def g = f(T=real)

When this is not sufficient, a whole package can be templatized

**quicksort.fy**

.. code-block:: fython

  import type_provider(target_class=T)

  def quicksort(x):
    T x(:)
    int i
    int res r 

    r = 0
    for i in [1, size(x)]:
      r += x[i].less_than(x[i+1])

  
**consumer.fy**

.. code-block:: fython

  import quicksort(*)
  ||type_provider = maxwell, target_class = Atom ||

  int r
  Atom a(10)
  r = quicksort(a)
