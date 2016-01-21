Imports
-------

Three kinds of imports are possible in Fython.
With a star import all the names are imported.
With an aliased namespace import,
the names of the target module are acessible through the alias.
With a slice import, only the stated names are imported, possibly aliased.

**imports.fy**

  .. literalinclude:: ../../example/stat/stat/imports/imports.fy

**imports_test.py**

  .. literalinclude:: ../../example/stat/stat/imports/imports_test.py

It is possible to import a directory when
it contains a ``__init__.fy`` file.
This is usefull as your package grow.
The content of our ``__init__.fy`` for the imports directory is

**__init__.fy**

  .. literalinclude:: ../../example/stat/stat/imports/__init__.fy

When importing a package, the main code of the package needs to be triggered manually. 
The main code of package is any code that is not part of a function
and that is not a specification (variable, class and interface specification).
