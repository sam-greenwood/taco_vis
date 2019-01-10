# core_flow
Python module for visualising torsional oscillations (and other 2D core flow data)


This module will take 2D polar coordinate data and create still plots or time varying animations of it, with a focus on torsional oscillations within a planetary interior.  Data can be simply contoured or (for torsional waves) be represented as differentially rotating cylinders in either 2D or 3D.


Animations can be generated from just 1 line of code, e.g.:

`import numpy as np`

`from core_flow import flow`

generate some random data:

`data = np.random.rand(10,10,10) #10 points in radius, azimuth and time`

load data into flow class:

`f = flow(data)`

plot the animation:

`f.plot_contours(animate=True)`


# Installation

Python 3 with numpy and matplotlib is required for this module to run. Clone this repository then either:
1. copy core_flow.py to your working directory (if you just want this accesible from that directory)
2. run the setup file with "python setup.py" from the command line (if you would like to add the module to the python path)



# Usage

data must be a 3D numpy array. The dimensions of the array correspond to the number of points in radius, azimuth and time repsectively. If for example you have data which does not depend on one of these (e.g. torsional wave data does not depend on azimuth), make the size of that dimension 1 but it must still be a 3D array, e.g.:

`import numpy as np`

`data = np.random.rand(10,10) #random data with 10 points in radius and time`

must be converted to a 3D array, e.g.:

`data = np.atleast_3d(data).reshape((10,1,10))`


The data is also assumed to be on a regular grid with radius in the domain [0,1] and azimuth between [0,2pi].


With that the 'flow' class can be initialised with the data:
`from core_flow import flow`

`f = flow(data)`


There are 3 types of plot available: contours, cylinders and cylinders_3D. The same 3 keyword arguments are available for each and do the same thing:

1. animate (default = False). If True then a matplotlib animation is created, iterating through the time axis of the data. If False then simply a static plot of one time interval of the data will be created.
2. save (default = False). If True then the image (if animate is False) or animation (if animate is True) will not be shown but instead saved to the current working directory.
3. time_idx (default = 0). If animate is False then this specifies the time index along the 3rd dimension of the data to be staically plotted.

#### contours

`flow.contours(self,animate=False,save=False,time_idx=0)`

The input data can vary in radius, azimuth and time, with a filled contour plot produced at each time interval. The colour scale is automatically scaled to the values within the data and to be symmetric about a value of 0.

#### cylinders

`flow.cylinders(self,animate=False,save=False,time_idx=0)`

The input data is angular velocity (radians per unit time) and depends on radius and time (azimuth dimension only has size 1). This produces a 2D plot with concentric circles representing concetric cylinders (with radii at the radial grid points in the data). A series of black dots are plotted on each cylinder and are advected to visualise the sense of rotation. The cylinders are coloured by the value of velocity at that time interval.

#### cylinders_3D

`flow.cylinders_3D(self,animate=False,save=False,time_idx=0)`

The same as 'cylinders' but instead the plot is a 3D representation of the cylidners within a sphere. Although the plot looks 3D it is actually rendered on 2D axes, circumventing the current bugs with drawing on 3D axes in matplotlib.


There are a few other settings which are saved as attributes in the 'flow' class which can be printed to the screen with the classes __call__ method, including: filenames for saved images/movies, fps of movies etc.
