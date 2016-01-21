Interface
---------

An interface is declared with the interface keyword

.. code-block:: fython

  interface:
    def f:
      real in x
      real res r

To facilitate the definition of C procedure
the modifier ``iso(c)`` can be used

.. code-block:: fython

  interface:
    def iso(c) f:
      real in x

The ``iso(c)`` modifier can be used on any function declaration
and is not restricted to interface declaration.
The effect of the modifier is to produce

.. code-block:: fortran

  !!!
  subroutine f(x) bind(c)
    use iso_c_binding
    real, intent(in) :: x
  end subroutine
  

