Python Syntax
~~~~~~~~~~~~~

Fython allows to write Fortran code
with Python syntax.
No messy ``end xyz`` everywhere.
No more ``%`` for object attributes, 
enjoy the ``car.color`` notation.
No more concatenation puzzle,
use multiline string ``"""xyz"""``.
No more ``&`` for multiline instruction,
simply use parenthesis 

.. code-block:: fython

  many(
    arguments,
    and,
    more,
  )

Write class with class, enjoying attribute getter and setter.

.. code-block:: fython

  class Nucleon(Atom):
    real position = 1 
    int weight = 10

    def pget fission:
      self inout
      self.weight /= 2

    Nucleon n
    n.fission
    print 'weight {:n.weight}'