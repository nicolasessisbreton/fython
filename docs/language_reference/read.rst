Read
----

You can read a file by specifying its url.
The extension is then assumed to be ``.out``

.. code-block:: fython

  read .data: x y z

You can specify a path in the file system with a string

.. code-block:: fython

  read './data.out': x y z

You are then free to use any extension you want.

The read statement in Fython supports csv-like formats automatically.
In Fortran, this is a called a list-directed read.
For this release, the other kind of read statement are not supported.

You can use the name of variable that does not contains a dot
for the read source

.. code-block:: fython

  char(100) data

  read data: x y z

If the name of the variable contains a dot, use the ``unit`` modifier

.. code-block:: fython

  read unit(mendeleiv.table): x y z

You can read into a vector or any other variable

.. code-block:: fython

  read .data:
    x[:, i]
    atom.name


