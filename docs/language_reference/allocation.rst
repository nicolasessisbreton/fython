Allocation
----------

Memory is allocated and deallocated with the ``alloc`` and ``dealloc`` keyword

.. code-block:: fython

  alloc: x y(n) z

  alloc(n):
    x
    y
    z(m)

  dealloc: x y z

When the keyword ``alloc`` has an argument, it is used
as the default size for any variable where no size is specified.