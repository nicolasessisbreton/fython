**Wrap Fortran code and shared library**

All intrinsic Fortran module are avalaible in Fython.
Other Fortran modules are avalaible 
once they are in your Python path

.. code-block:: fython

  import iso_c_binding(*)
  import fftw.discrete_cosine_transform(*)

  real x(10)
  fftw_dct(x)

Putting a Fortran module in the Python path is usually done with

.. code-block:: python

  import sys
  sys.path.append('~/fftw')

A Shared library can be imported once you have
a Fortran or a Fython interface for it

.. code-block:: fython

  import mkl.include.mkl_vsl
  import mkl.lib.intel64.libmkl_intel_lp64

The first import is the fortran interface ``mkl_vsl.f90``.
The second import is for the shared object library ``libmkl_intel_lp64.so``.

The requirement for these imports to work
is that the mkl root directory must be in your Python path.
This is usually achieve with

.. code-block:: python

  import sys
  sys.path.append('/opt/intel')

