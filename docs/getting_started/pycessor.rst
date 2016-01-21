Pycessor
--------

A Pycession is the fythonic term for Python preprocessor interpolation.

Pycessions can be used to define compile time constant
or to avoid writing lines of code that are similar.

Since any Python code is allowed in pycession,
a more exotic usage can be to run a Makefile script
that produce a shared library used in your module.

For clarity, we write python imports together with the
other fython imports at the top of a module.

  **pycessor.fy**

  .. literalinclude:: ../../example/stat/stat/pycessor/pycessor.fy

  **pycessor_test.py**
  
  .. literalinclude:: ../../example/stat/stat/pycessor/pycessor_test.py


When a pycession is an expression such as ``1+2`` or ``f(1)``,
its returned value is inserted in your fython code.
When a pycession contains several lines,
you need to explicitly state wich string to include in your code.
The special pycessor function ``write`` serves this purpose.

