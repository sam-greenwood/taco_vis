"""
Randomly Generated Data
~~~~~~~~~~~~~~~~~~~~~~~

From the README.
"""
import numpy as np
from taco_vis import FLOW

# Import and generate some random data
data = np.random.rand(10,10)

f = FLOW(data)
# Create instance of FLOW class and use it to plot an animation.
f.plot_cylinders_3D(animate=True)

###############################################################################
# This produces a 2D plot of a slice through the equitorial plane with
# concentric circles representing the concentric cylinders (with as many
# cylinders as there are radial grid points in the data). A series of black
# dots are plotted on each cylinder and are advected to visualise the sense of
# rotation. The cylinders are coloured by the value of velocity at that time
# interval.

f.plot_cylinders(animate=False, save=False, time_idx=0)

###############################################################################
# The same as 'cylinders' but instead the plot is a 3D representation of the
# cylinders within a spherical core.

f.plot_cylinders(animate=False, save=False, time_idx=0)

###############################################################################
# A filled contour plot of the data is produces, which does not strictly need
# to be axisymmetric and hence the data array may be 3D (radius, theta, time).

f.plot_contours(animate=False, save=False, time_idx=0)

###############################################################################
# Default settings for the appearance of the plots are attributes of the FLOW
# class. Current settings can be seen by the call method of the class:
print(f())
