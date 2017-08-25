Variable Declaration
--------------------

In Fython the elementary types have a Python flavor

.. code-block:: fython

  real x
  int y
  char z
  bool a
  complex b

Constant are declared with the attribute ``cons``.

.. code-block:: fython

  real cons x

Classes are instantiated by using there name

.. code-block:: fython

  class A:
    pass

  A a

String variable can be assign a value with a multiline string

.. code-block:: fython

  char(100) x

  x = """
    extra leading space
    at the beggining remove
  """

  x = '''
    triple quote
  '''

  x = 'single line'
  x = "double quote"

Any newline or tab character in the string will be honored.

For procedure argument, use the ``proc`` modifier

.. code-block:: fython
  interface:
    def worker:
      pass

  def consummer:
    proc(worker) f
    f() 
      