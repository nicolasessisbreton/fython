The Host Python package
---------------------------

First, we create the folder structure for the Python package
where our Fython package will reside

  .. literalinclude:: stat_package_structure
  :language: shell

The content of ``setup.py`` is

  .. literalinclude:: ../../example/stat/setup.py
  :language: python

We register the package in Python with

.. code-block:: shell

  python3 setup.py develop

