Class
-----

A class is defined with the ``class`` keyword.

.. code-block:: fython

  class A:
    real x

    def f:
      self in
      real res r
      r = self.x

    def pget y:
      s in
      real res r
      r = s.x

    def pset y:
      s inout
      real in value
      s.x = value

The first argument of any class method must be the ``self`` argument.
The name used for the ``self`` argument can be anything.
Above we used ``s`` instead of ``self`` for the getter and setter.

Getter and Setter are defined with the ``pget`` and ``pset`` modifiers.

Inheritance is indicated with parenthesis after the class name

.. code-block:: fython

  class C(B, A):
    pass

You can separate the specification and the implementation of a class
with the spec interpolation

.. code-block:: python

  # spec.fy

  class A:
    real x
    def pure f:
      self in
      real res r

  # code.fy
  import spec(*)

  class A:
    def f:
      r = self.x + 10

You can explicitly state the spec to use with the spec modifier

.. code-block:: fython

  class A:
    real x

  class spec(A) B:
    pass

You can use the ``inline`` statement to include verbatim the definition of
a class or a function into your class

.. code-block:: python

  class A:
    real x 

  class B:
    inline A