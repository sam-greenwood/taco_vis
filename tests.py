import core_flow as cf
import numpy as np
import matplotlib.pyplot as plt

########################
#Create example dataset:
def flow_func(radius,theta,time):
    u = np.sin(2*np.pi*radius) * np.sin(theta) * np.sin(2*np.pi*time)
    return u

time = np.linspace(0,1,50)
radius = np.linspace(0,1,10)
theta = np.linspace(0,2*np.pi,50)

TH,R,T = np.meshgrid(theta,radius,time)
data = flow_func(R,TH,T)

#Read data into flow class
f = cf.flow(data)

#Output movie and images should be the same as contained in the 'test_files' folder of this repo.

#Test contour plot_contours
f.colorbar_title = 'Non-dimensional\nvelocity'
f.movie_filename = 'test_contour.mp4'
f.plot_contours(animate=True,save=True)
plt.close('all') #If plotting another image, close this animation figure first.


#Test 2D datasets plots
data = data[:,14,:] #take a slice in theta and retain a 3D array
f = cf.flow(data)

#Resize number of theta points
f.th_resolution = 10

#Test contour plot_contours
f.colorbar_title = 'Non-dimensional\nvelocity'
f.image_filename = 'test_contour.png'
f.plot_contours(save=True,time_idx=14)
plt.close('all') #If plotting another image, close this animation figure first.



f.image_filename = 'test_cylinders.png'
f.colorbar_title = 'Non-dimensional\nvelocity'
f.plot_cylinders(save=True,time_idx=14)
plt.close('all')

f.image_filename = 'test_cylinders_3D.png'
f.plot_cylinders_3D(save=True,time_idx=14)
plt.close('all')
