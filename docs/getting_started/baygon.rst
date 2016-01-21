Baygon
------

When an error occurs in your code,
Fython will usually detect it and produce a stack trace.

  **baygon.fy**

  .. literalinclude:: ../../example/stat/stat/baygon/baygon.fy

  **baygon_test.py**

  .. literalinclude:: ../../example/stat/stat/baygon/baygon_test.py

If Fython error detection system is overriden by 
your compiler or simply fails,
you can use the verbose function of a Fython module,
The verbose function tells Fython to print the location
of every line of code that are run.
You can then easily spot that wonderfull bug.


  **verbose_test.py**

  .. literalinclude:: ../../example/stat/stat/baygon/verbose_test.py

Sometimes Fython may fails to detect changes in your code
since the last compilation. If that happens, simply load your module
with the ``force`` option to trigger a refresh of the Fython cache
  
  **force_test.py**

  .. literalinclude:: ../../example/stat/stat/baygon/force_test.py

When your code is bug free, the ``release`` keyword
tells Fython to run your code at full Fortran speed,
with all optimizations enables


  **release_test.py**
  
  .. literalinclude:: ../../example/stat/stat/baygon/release_test.py