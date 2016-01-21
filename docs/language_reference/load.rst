Load Function
--------------

The python api side ``load`` function has the following default arguments

.. code-block:: python

  #>>>
  load(
    fython_module_url,
    force = 0,
    release = 0,
  )

The ``force`` argument is used to force a refresh of the Fython dependency cache.

The ``release`` argument indicates wheter to run in debugging mode (``0``),
or release mode (``1``).
In debug mode, Fython tries to detect errors.
In release mode, all the compiler optimization are enabled.

When a Fython module is loaded, you access its objects with there name.

.. code-block:: python

  #>>>
  from fython import *
  m = load('.mean')

  x = m.global_variable()
  y = m.global_variable_with_explicit_shape(shape=[10])

  # function call
  m.mean(x, y)

  # keyword call
  m.mean(
    offset = x,
    vec = y,
  )


When a global variable is accessed, Fython will automatically determine its fytype.
For function however, only minimal arguments consistency is made.
You should make sure that you invoke your Fython function with
the right argument order and the right fytype.
The argument order consistency can be alleviated by using a keyword argument call.
Fython will then call your Fython function with the argument in the right order.