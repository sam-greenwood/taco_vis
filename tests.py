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


#Check potential error with movie writer executible file path needing to be specified.
print('-------------')
print('animation writer is set to: '+plt.rcParams['animation.writer'])
text = 'animation.'+plt.rcParams['animation.writer']+'_path'
try:
    print('The path to this writer\'s executible is: '+plt.rcParams[text])
    print('If saving an animatino errors, you may need to set the matplotlib.pyplot.rcParams['+text+'] variable to the correct path')
    print('e.g. \'plt.rcParams[\'animation.ffmpeg_path\'] = \'/usr/local/bin/ffmpeg\'\'')
    print('-------------')
except:
    raise ValueError('Encoder not recognised. Should be set to ffmpeg (recommended) or menconder')



#Test contour plot_contours
f.colorbar_title = 'Non-dimensional\nvelocity'
f.movie_filename = 'test_contour.mp4'
f.plot_contours(animate=True,save=True)
plt.close('all')


#Test cylindrical plots
data = data[:,14,:].reshape((10,1,50)) #take a slice in theta and retain a 3D array
f = cf.flow(data)

f.colorbar_title = 'Non-dimensional\nvelocity'
f.plot_cylinders(time_idx=14)
plt.close('all')

f.plot_cylinders_3D(time_idx=14)
plt.close('all')
