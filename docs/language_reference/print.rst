Print
-----

Printing to the console needs no modifier

.. code-block:: fython

  print 'x {:x}'

When an url is used the file extension is assumed to be ``.out``

.. code-block:: fython

  print .simulation 'x {:x}'

A file system path can also be used

.. code-block:: fython

  print './simulation.out' 'x {:x}'

You can then choose any extension you want.

You can print to a character variable when its name does not contain a dot

.. code-block:: fython

  char(100) r

  print r 'x {:x}'

If the name contains a dot use the ``unit`` modifier

.. code-block:: fython

  print unit(atom.name) 'proton'

The unit modifier can also be used if you opened a file by yourself

.. code-block:: fython

  int u = 10
  open(unit=u, file='./simulation.out')
  print unit(u) 'x {:x}'

If you use a number, the unit modifier is not necessary

.. code-block:: fython

  print 10 'x {:x}'

You can control the mode in which the file is written to during a print statment
with the mode modifier

.. code-block:: fython

  print mode(a) 'x {:x}'

  print mode(w) 'overwrite any previous content'

The default mode is ``a``.

The format mini-language is that of Fortran plus two additions

.. code-block:: fython

  print """
    {:x} : general format used
    {f5.2:x} : float format
    {i5:x} : int format

    {v:y} : vector format: [1, 2, 3, ]

    {vc:y} : vector content format: 1, 2, 3,
  """

The additions are the ``v`` and ``vc`` formats that facilitates the printing of vectors.


If a print statement is used only in debug mode, use the ``xip`` instruction

.. code-block:: fython

  xip 'printed only in debug mode'
  print 'printed in both debug and release mode'

The ``xip`` takes the same modifiers than the ``print`` instruction.
The ``xip`` instruction is usefull for debugging.
