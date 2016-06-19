Imports
-------

Three kinds of imports are possible in Fython.
Aliased namespace import, star import and slice import.

.. code-block:: fython

  import pca
  import stat.mean = m

  import stat.variance(*)
  import stat.newspaper(x, y=z)

When the module url is composed of only one name,
such as the ``pca`` imports.
The statement is equivalent to

.. code-block:: fython

  import pca = pca

With an aliased namespace import, the object in the 
module are access with a dot ``.``

.. code-block:: fython

  import stat.mean = m
  m.cube_mean(1, 2, 3)

With a star import all the object of the imported module are avalaible

.. code-block:: fython

  import stat.mean(*)
  cube_mean(1, 2, 3)

With a slice import only the stated names are imported, optionally aliased

.. code-block:: fython

  import stat.mean(cube_mean, char_mean= cm)
  cube_mean(1, 2, 3)
  char_mean('abc', 'def', 'ijk')


For all imports it is necessary that you have write permission
to the directoty that contains the imported module.
This is because Fython needs to maintain build products in the same directory.
The only exception to this rule are shared library import,
as no build product needs to be maintained in these case.

The url of a module is its qualified Python name

.. code-block:: fython

  import numpy.random.uniform

This implies that for a file to be importable,
it must be on your Python path.

The first way to put a file
on your Python is
to create a host Python package and registering it
to Python with a setup script

.. code-block:: shell

  $ python3 setup.py develop

See the Getting Started section for the details.

The other method
is to modify your path directly 

.. code-block:: python

  #>>>
  import sys
  import fython
  sys.path.append('/opt/nag')
  m = fython.load('random.sobolev')

In a Python url, the file extension cannot be part of the url.
You should then take into account the following resolution order.
In a compile time import, Fython first search for

- a Fython file (``.fy, __init__.fy``)
- a Fortran file (``.f90, .f03, ...`` and many other)
- a So File (``.so``)

In a pycessor time import, Fython search for

- a Python file (``.py, __init__.py``).

For print and read statement that uses an url,
the assumed extension is ``.out``.

For Fortran, only star and slice imports are allowed.
For So only star imports are allowed.