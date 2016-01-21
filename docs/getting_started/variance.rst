Variance
--------

In Fython the specification and the implementation of a function or a class
can be separated.
Similar to Python, we start by working on our implementation
of the variance function,
deferring the spec to the ``variance_spec`` import

**variance.fy**

  .. literalinclude:: ../../example/stat/stat/variance/variance.fy

When we are satisfied with our algorithm, we write the specification

**variance_spec.fy**

  .. literalinclude:: ../../example/stat/stat/variance/variance_spec.fy

The specification contains all the imports and the definitions we need in
``variance.fy``.
We test with

**variance_test.py**

  .. literalinclude:: ../../example/stat/stat/variance/variance_test.py

What we did above is called an implicit spec interpolation.
We can also do explicit spec interpolation with the ``spec`` modifier

**explicit_spec_interpolation.fy**

  .. literalinclude:: ../../example/stat/stat/variance/explicit_spec_interpolation.fy

We test with

**explicit_spec_interpolation_test.fy**

  .. literalinclude:: ../../example/stat/stat/variance/explicit_spec_interpolation_test.py