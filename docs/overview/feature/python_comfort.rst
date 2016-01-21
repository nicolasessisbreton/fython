Python Comfort
~~~~~~~~~~~~~~

Fython import system is modeled after Python.
You can define Fython modules accross several folders.
They will all correctly compile and link.

.. code-block:: fython

  import .variance = var
  import stat.mean(*)
  import .svm(vapnik, least_square_svm=lsq_svm)

Fython has a stack trace for fast error spotting.
Say goodbye to those uninformative runtime errors.

.. code-block:: shell

  fython sigsegv: segmentation fault

  module stat.buggy
  function subboom
  line 7

  stack trace (lineno function module) (most recent first)

  7 subboom   stat.buggy
  3 boom      stat.buggy


Fython ``print`` and ``read`` function are intuitive.
The format mini-language is that of Fortran plus several improvements.
Interpolating variables can be specified directly in the string like Perl.

.. code-block:: fython

  print './out' 'x is {:x}'

  print .file 'column 2 is {v:x[:,2]}

  read .data: x y z