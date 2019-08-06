import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

from core_flow import flow

############################################################################
#EXAMPLE 1

########################
#Create some data:
def flow_func(radius,theta,time):
    u = np.sin(2*np.pi*radius) * np.sin(theta) * np.sin(2*np.pi*time)
    return u
u = np.zeros((100,50,200))
r,th,t = u.shape

time = np.linspace(0,1,t)
radius = np.linspace(0,1,r)
theta = np.linspace(0,2*np.pi,th)

for i in range(r):
    for j in range(th):
        u[i,j,:] = flow_func(radius[i],theta[j],time)
########################



#Initialise flow class
f = flow(u)

#Use __call__ method to print user parameters
f()

#Change output dpi and image/movie filenames from defaults
f.dpi = 300
f.movie_filename = 'example_contour.mp4'

#Plot the animation of the data and then save it as a movie (once figure is closed)
f.plot_contours(animate=True)
plt.close('all') #If more plots are to be made in the script, advised to close the previous figure first

f.plot_contours(animate=True,save=True)
plt.close('all')



############################################################################
#EXAMPLE 2

########################
#Create some data:

#Read in Grace's dataset
data_file = './cox_etal_2014.txt'  #Data file
data = np.genfromtxt(data_file,delimiter=',')

#Regrid the data down (too high resolution to be practically plotted as is)
r   , t      = np.linspace(0,1,data.shape[0]), np.linspace(0,1,data.shape[1])
time, radius = np.linspace(0,1,2000)         , np.linspace(0,1,16)

test = scipy.interpolate.RectBivariateSpline(r,t,data)
u = test(radius,time)
u = np.atleast_3d(u).reshape((radius.size,1,time.size))
#reshaping data into required 3D format, with only 1 point in theta
#(code will assume this means it is the same for all theta)
########################



#Initialise flow class
f = flow(u)

#Up the speed of rotation (factor applied to advection of texture)
f.speed = 5

#By default, first time index is used to plot images.
f.plot_cylinders()
plt.close('all')

#Can use the time_idx keyword to specify otherwise (doesn't do anything to animations)
f.plot_cylinders(time_idx=400)
plt.close('all')


f.plot_cylinders(animate=True)
plt.close('all')

#2 different types of cylindrical plot for torsional wave visualisation
f.plot_cylinders_3D(animate=True)
