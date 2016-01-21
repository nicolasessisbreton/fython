Installation
============

Fython can be installed with

.. code-block:: shell

  git clone https://github.com/nicolasessisbreton/fython
  cd fython
  python3 setup.py install

To use Fython, a Fortran compiler must be present on your system.
By default, Fython will try to use gfortran or ifort.
If you want to explicitly specify one of these you can do

.. code-block:: python

    import fython

    fython.use_ifort()
    fython.use_gfortran()

To use another compiler do

.. code-block:: python

    import fython

    fython.set_compiler(
        cmd = 'gfortran'
        prefix = '__',
        infix = '_MOD_',
        suffix = '',
        debug = '-O0',
        release = '-O3',
        error_regex = '(Error:|ld:)'
    )

Assuming

.. code-block:: shell

    nm -D gfortran_produced.so

show names as

.. code-block:: shell

    __modname_MOD_varname

that is the pattern

.. code-block:: shell

    prefix modname infix varname suffix

Testing it
----------

That's it.
Your Fython rocket is ready

.. code-block:: python

    >>> import fython
    >>> fython.hello()
    'Welcome to Fython. See the build products in ./__fycache__'

Syntax Highlighting in Sublime
------------------------------

To get syntax highlighting in Sublime Text,
you can use these
`files <https://github.com/nicolasessisbreton/fython/sublime_syntax_definition>`_.