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

The spec for ``f`` can be in the same module or originate from an import.
You can also explicitlye specify the spec to use with the ``spec``.

.. code-block:: fython

  def elemental f:
    real in x
    real res r

  def spec(f) g:
    r = x + 10

    def spec(f, g) h:
      pass # multiple spec parent
      
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
  inline release f

When no modifier is specified, the code is inlined in all compilation mode.

Automatic argument completion
dispense for the need to 
write all the arguments of a function
provided
the name of the argument
is the same than a name in the current scope.

.. code-block:: fython

  real x = 1
  real y = 10

  def f:
    real in x
    real in y

  f(y=1.) # x added automatically
  f() # both x and y added

Automatic arguments completion
works for keyword arguments call only.
It cannot be mixed 
with positional argument code.

.. code-block:: fython

 # with f as above 

 f(y) # not supported
 f(y=1.) # supported


If a function should not be compiled,
used the ``noprod`` modifier.
This is usefull when the function is only used as a spec provider,
and that the function should not be compiled.

.. code-block:: fython

  def noprod f:
    real x(n) # n is not defined, this would give an error if compiled

  def spec(f) g:
    int in n

    x += 1 # definition of x is provided by the spec of f

The ``noprod`` modifier is not inherited
during a spec interpolation.
So, only ``f`` is not compiled.
To not compile ``g``, explicitly use the modifier ``noprod``.

to help distinguish between pure and non-pure function used the modifiers
``pure`` and ``sidef``

.. code-block:: fython

  def pure f:
    pass

  def sidef g:
    pass

The modifier ``sidef`` has no effect during compilation.
The modifier clearly states the intent of the coder:
that the function ``g`` has side-effects,
and cannot be marked as pure.