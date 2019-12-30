
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   self
   README
   examples/index


Torsional Axisymmetric Core Oscillations Visualiser (TACO-VIS)
==============================================================
A python module for animating torsional wave data for fluid planetary cores.

TACO-VIS provides a simple set of python visualisation tools for fluid flow velocity data from fluid planetary interiors with a focus on animating torsional wave models. TACO-VIS is a lightweight module built only upon the common numpy/matplotlib python packages and is free to be used and modified as the user requires.

Animations can be generated simply and quickly with minimal lines of code, e.g.:

.. code-block::

  import numpy as np
  from taco_vis import FLOW

  # Import and generate some random data
  data = np.random.rand(10,10)

  f = FLOW(data)
  # Create instance of FLOW class and use it to plot an animation.
  f.plot_cylinders_3D(animate=True)

.. image:: ./paper/images/example_cylinders_3D.png
   :width: 450pt


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
