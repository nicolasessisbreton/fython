Backus
--------

You can import a Fortran module in Fython.
For this example, we use the ``writer`` function of Fython.

  **fortran.py**

  .. literalinclude:: ../../example/stat/stat/backus/fortran.py

The ``writer`` function turns a Python script into a playground
for languages.
The function creates the file ``.brent.f90`` in the current directory.
The content of the file is the indented content after the file name.

What we did is that we created the file ``brent.f90`` and the file
``consummer.fy``.
The Fython ``consummer`` module imports the Fortran ``brent`` module.
We then test the Fython ``consummer`` module with the ``load`` function.

we can also imports shared library in Fython

  **so.py**

  .. literalinclude:: ../../example/stat/stat/backus/so.py

In ``ritchie``, we use the ``bind(c)`` attribute
to emulate the standard naming convention in shared library.
We then compile ``ritchie`` into a shared library with gfortran.
After that we load the Fython module ``backus`` into Python.
The ``backus`` module then places a class to ``compile``.
