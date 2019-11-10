import taco_vis as tv
import numpy as np
import matplotlib.pyplot as plt
import os


########################
# Create example dataset:
def flow_func(radius, theta, time):
    u = np.sin(2 * np.pi * radius) * np.sin(theta) * np.sin(2 * np.pi * time)
    return u


time = np.linspace(0, 1, 50)
radius = np.linspace(0, 1, 10)
theta = np.linspace(0, 2 * np.pi, 50)

TH, R, T = np.meshgrid(theta, radius, time)
data = flow_func(R, TH, T)

# Read data into flow class
f = tv.FLOW(data)

assert np.min(f.data) < 0, 'Data has no negative values'
assert np.max(f.data) > 0, 'Data has no positive values'


# Test animate contour plot_contours
f.colorbar_title = "Non-dimensional\nvelocity"
f.movie_filename = "test_contour.mp4"
f.plot_contours(animate=True, save=True)
# If plotting another image, close this animation figure first.
plt.close("all")
assert os.path.isfile(f.movie_filename), 'File {} does not exist after saving'.format(f.movie_filename)


# Test contour plot_contours
f.colorbar_title = "Non-dimensional\nvelocity"
f.image_filename = "test_contour.png"
f.plot_contours(save=True, time_idx=14)
# If plotting another image, close this animation figure first.
plt.close("all")
assert os.path.isfile(f.image_filename), 'File {} does not exist after saving'.format(f.movie_filename)


#Create axisymmetric data
data_axisym = flow_func(R, np.pi/2, T)

f_axisym = tv.FLOW(data_axisym)

f_axisym.image_filename = "test_cylinders.png"
f_axisym.colorbar_title = "Non-dimensional\nvelocity"
f_axisym.plot_cylinders(save=True, time_idx=14)
# If plotting another image, close this animation figure first.
plt.close("all")
assert os.path.isfile(f_axisym.image_filename), 'File {} does not exist after saving'.format(f_axisym.movie_filename)


f_axisym.image_filename = "test_cylinders_3D.png"
f_axisym.plot_cylinders_3D(save=True, time_idx=14)
# If plotting another image, close this animation figure first.
plt.close("all")
assert os.path.isfile(f_axisym.image_filename), 'File {} does not exist after saving'.format(f_axisym.movie_filename)
