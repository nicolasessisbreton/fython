Newspaper
-----------------

Any good bug is remove by several usage of the print statement.
With Fython the print statement output can be standard out,
a file on the Python path, or a path on the file system

**print.fy**

  .. literalinclude:: ../../example/stat/stat/newspaper/print.fy

The Python url `.x_final` tells Fython to create a file 'x_final.out'
in the same directory than the Fython module.
A string can also be used to specify the path.

**print_test.fy**

  .. literalinclude:: ../../example/stat/stat/newspaper/print_test.py

Since all bugs originates from data,
we use the read statement to keep ourselves busy

**read.fy**

  .. literalinclude:: ../../example/stat/stat/newspaper/read.fy

The possible mode for printing to files are ``mode(a)`` for appending,
and ``mode(w)`` for overwriting.
The default mode is appending.
We test with

**read_test.py**

  .. literalinclude:: ../../example/stat/stat/newspaper/read_test.py

