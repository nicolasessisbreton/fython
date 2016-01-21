Function
----------

A function is declared with the keyword ``def``

.. code-block:: fython

  def f:
    real in x
    real res r

For a variable to be recognized as an argument, it must have one
of the intent modifier

.. code-block:: fython

  in
  out
  inout

The return value of a function must be indicated with the modifier

.. code-block:: fython

  res

When no argument has the modifier ``res``, the function has no return value.

You can separate the implementation and the specification of you function with spec interpolation

.. code-block:: fython

  def pure f:
    real in x
    real res r


  def f:
    r = x + 3

The spec for ``f`` can be in the same module or originated from an import.
You can also explicitlye specify the spec to use with the ``spec``.

.. code-block:: fython

  def elemental f:
    real in x
    real res r

  def spec(f) g:
    r = x + 10

You can use the ``inline`` instruction to include verbatim the definition
of one function into another

.. code-block:: fython

  def f:
    x += 1

  def g:
    inline f

The modifier ``debug`` or ``release`` can be use to specify in which mode to include
the code.
This is usefull for conditional inclusion of logging code for example.

.. code-block:: fython

  inline debug f
  inlinde release f

When no modifier is specified, the code is inlined in all compilation mode.
