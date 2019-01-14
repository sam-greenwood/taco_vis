# core_flow
Python module for visualising torsional oscillations (and other 2D core flow) for a planetary interior


This module will take 2D polar coordinate data and create still plots or time varying animations of it, with a focus on torsional oscillations.  Data can be simply contoured (for any 2D dataset) or be represented as differentially rotating cylinders in either 2D or 3D (for torsional wave data only).

<p align="center">
  <img src="paper/images/example_contour.png" width="450" align="left" />
  <img src="paper/images/example_cylinders_2D.png" width="450" align="left" />
  <img src="paper/images/example_cylinders_3D.png" width="450" align="left" />
</p>



Animations can be generated simply and quickly with minimal lines of code, e.g.:

`import numpy as np`

`from core_flow import flow`

`data = np.random.rand(10,10,10)` generate some random data

`f = flow(data)` load data into flow class

`f.plot_contours(animate=True)` plot the animation


# Installation

Python 3, numpy and matplotlib (and ffmpeg to save movie files) are required for this module to run. Clone this repository then either:
1. copy core_flow.py to your working directory (if you just want this accesible from that directory) and install the required dependencies
2. run the setup file with "python setup.py" from the command line, installing the module and it's dependencies.

# Dependencies
1. Python 3
2. numpy
3. matplotlib
4. ffmpeg (for saving animations as movie files)




# Usage

data must be a 3D numpy array. The dimensions of the array correspond to the number of points in radius, azimuth and time repsectively. If for example you have data which does not depend on one of these (e.g. torsional wave data does not depend on azimuth), make the size of that dimension 1 but it must still be a 3D array, e.g.:

`import numpy as np`

`data = np.random.rand(10,10)` random data with 10 points in radius and time must be converted to a 3D array, e.g.:

`data = data.reshape((10,1,10))`


The data is also assumed to be on a regular grid with radius in the domain [0,1] and azimuth between [0, 2pi].


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

---

There are a few other settings which are saved as attributes in the 'flow' class which can be printed to the screen with the class __call__ method, including: filenames for saved images/movies, fps of movies etc.


# Known issues

You may run problems with matplotlib interfacing with ffmpeg to save animations.

If you get something along the lines of: `ValueError: Invalid file object: <_io.BufferedReader name=X>` where `X` is some number, your binary of ffmpeg may not be working. This can be common if you are using an environment manager, such as anaconda and may be solved by installing the ffmpeg binary to your system yourself and setting: `matplotlib.pyplot.rcParams['animation.ffmpeg_path'] = '/usr/local/bin/ffmpeg'` (or wherever you have installed it)
immedietly after `import matplotlib` to force it to use that one, rather than the ffmpeg inside the anaconda path.
