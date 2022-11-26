.. pysumreg documentation master file, created by
   sphinx-quickstart on Fri Nov 25 10:34:29 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pysumreg
=========

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   sum_registers

:release:   |release|
:version:   |version|
:published: |today|

Examples
========

We start these examples by first creating a set of registers:

.. code-block:: python
   :linenos:

   import pysumreg
   reg = pysumreg.SummationRegisters()

Mean and Standard Deviation
----------------------------

Find the mean and standard deviation of a set of ordered pairs:

.. code-block:: python
   :linenos:

   reg.clear()
   reg.add(1, -1)
   reg.add(2, -2)
   reg.add(3, -3)
   print(f"{reg.mean_x=}")
   print(f"{reg.stddev_x=}")
   print(f"{reg.mean_y=}")
   print(f"{reg.stddev_y=}")

which prints these results::

   reg.mean_x=2.0
   reg.stddev_x=1.0
   reg.mean_y=-2.0
   reg.stddev_y=1.0

Linear Analysis
---------------

Using the same data as above, assess if this is a good linear fit. The
correlation coefficient provides a measure of the correlation between the
:math:`x` and :math:`y` values.  Value of 1.0 indicates an exact fit to a
straight line with positive slope (-1 means anti-correlated: a negative straight
line).  Zero means that the :math:`x` and :math:`y` values are not correlated,
no linear fit.

.. code-block:: python
   :linenos:

   reg.clear()
   reg.add(1, -1)
   reg.add(2, -2)
   reg.add(3, -3)
   print(f"{reg.correlation=}")
   print(f"{reg.intercept=}")
   print(f"{reg.slope=}")

which prints these results::

   reg.correlation=-1.0
   reg.intercept=0.0
   reg.slope=-1.0

Peak Analysis
---------------

Assuming that the data might represent a peak, compute parameters describing its
center and width.  We obtain the width (:math:`~2\sigma_c`) from the variance
(:math:`\sigma_c^2`) of the :math:`x` values weighted by the :math:`y` values.

.. code-block:: python
   :linenos:

   reg.clear()
   reg.add(1, 0)
   reg.add(2, 1)
   reg.add(3, 0)
   print(f"{reg.max_y=}")
   print(f"{reg.centroid=}")
   print(f"{reg.sigma=}")

which prints these results::

   reg.max_y=1
   reg.centroid=2.0
   reg.sigma=0.0

With only three values, it's an exact fit to the underlying statistical model of
the variance. We need more data (with :math:`y` values that are not zero) to
obtain a non-zero :math:`\sigma_c`:

.. code-block:: python
   :linenos:

   reg.add(1.5, 0.5)
   reg.add(2.5, 0.5)
   print(f"{reg.max_y=}")
   print(f"{reg.centroid=}")
   print(f"{reg.sigma=}")

which prints these results::

   reg.max_y=1
   reg.centroid=2.0
   reg.sigma=0.3535533905932738

Summary
--------

Print the entire contents of the summation registers object:

.. code-block:: python

   reg

which prints these results (re-formatted for display here)::

    SummationRegisters(
      X=10.0,
      XX=22.5,
      XXY=8.25,
      XY=4.0,
      Y=2.0,
      YY=1.5,
      centroid=2.0,
      correlation=0.0,
      intercept=0.4,
      max_x=3,
      max_y=1,
      mean_x=2.0,
      mean_y=0.4,
      min_x=1,
      min_y=0.5,
      n=5,
      sigma=0.3535533905932738,
      slope=0.0,
      stddev_x=0.7905694150420949,
      stddev_y=0.4183300132670378,
      x_at_max_y=2
    )

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`