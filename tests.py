import taco_vis as tv
import numpy as np
import matplotlib.pyplot as plt

print('Output movie and images should be the same as contained in the \'test_files\' folder of this repo')

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
f = tv.FLOW(data)


#Test contour plot_contours
f.colorbar_title = 'Non-dimensional\nvelocity'
f.movie_filename = 'test_contour.mp4'
f.plot_contours(animate=True,save=True)
plt.close('all') #If plotting another image, close this animation figure first.


#Create class
f = tv.FLOW(data)

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
