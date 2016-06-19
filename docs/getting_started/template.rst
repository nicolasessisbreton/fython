Template
--------

Function template are usefull to create overload
of a function

  **function.fy**

  .. literalinclude:: ../../example/stat/stat/template/function.fy

  **function_test.py**

  .. literalinclude:: ../../example/stat/stat/template/function_test.py

The template function needs to me marked with the modifier ``temp``.
The principle is the same for class

  **class.fy**

  .. literalinclude:: ../../example/stat/stat/template/class.fy

  **class_test.py**

  .. literalinclude:: ../../example/stat/stat/template/class_test.py

You can also templatize a whole package

  **package.fy**

  .. literalinclude:: ../../example/stat/stat/template/package.fy

When the module ``quicksort`` and all of its dependency is imported any occurence
of ``type_provider`` and ``target_class`` will be replaced
by the package interpolation provided at the import statement. 

The content of ``quicksort`` is

  **quicksort.fy**

  .. literalinclude:: ../../example/stat/stat/template/quicksort.fy

To prevent any package interpolation to happen during the import of ``type_provider``,
the import has the ``asis`` modifier.

We test with

  **package_test.py**
  
  .. literalinclude:: ../../example/stat/stat/template/package_test.py
