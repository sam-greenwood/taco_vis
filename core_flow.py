import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
plt.rcParams['animation.ffmpeg_path'] = '/usr/local/bin/ffmpeg' #If using ffmpeg to encode, file path to executible must be specified here.
import matplotlib.animation as anim

########################################################################################

class flow:

    def __init__(self,data):

        '''
        Initialise flow_class with a given data set.

        Parameters
        ----------
        data: 3D numpy array where the values represent angular velocity. The shape of the
        array should represent the number of data points in radius, theta and time respectively

        e.g. if shape(data) = (5,10,20), then there are assumed 5 points in radius, 10 in theta
        and 20 in time.
        '''

        a = data.shape

        #Assume radius, theta and time arrays
        self.data = data
        self.radius = np.linspace(0,1,a[0])
        self.theta = np.linspace(0,2*np.pi,a[1])
        self.time = np.linspace(1,a[2],a[2])

        #Default Settings
        self.speed = 1

        self.colorbar_title = 'velocity'
        self.title = 'time: %3.1f years'

        self.movie_filename='output.mp4'
        self.image_filename='output.png'
        self.dpi=200
        self.fps=24

        self.c_scale = np.max(np.abs(data[:]))


        #Assume that if only 1 point in theta is given, flow is not theta dependant.
        #Add in more theta points purely for contour plotting resolution

        if a[1] == 1:

            th_resolution = 50

            theta = np.linspace(0,2*np.pi,th_resolution)
            temp = np.zeros((a[0],th_resolution,a[2]))
            for i in range(a[0]):
                for j in range(a[2]):
                    temp[i,:,j] = data[i,0,j]*np.ones(theta.size)

            self.data = temp
            self.theta = theta

    #################################

    def __call__(self):

        '''
        Print the current settings of the flow class
        '''

        def print_setting(self,settings_txt):
            print(settings_txt+' : '+str(getattr(self,settings_txt)))

        settings = ['speed','colorbar_title','title','movie_filename','image_filename','dpi','fps','c_scale']

        print('\nCURRENT SETTINGS ---------------')
        for i in settings:
            print_setting(self,i)
        print('--------------------------------')

    #################################

    def plot_cylinders(self, animate=False, save=False, time_idx=0):

        '''
        Method for plotting flow as concentric cylinders e.g. for torsional oscillations

        Keyword arguments:

            'animate' - bool. If True will animate the plot (default: False)
            'save'    - bool. If True the plot will be saved rather than plotted (default: False)

        '''


        #Load in variables from self
        data = self.data
        time = self.time
        radius = self.radius

        speed = self.speed

        movie_filename = self.movie_filename
        image_filename = self.image_filename
        dpi=self.dpi
        fps=self.fps


        if save and animate:
            self.progress = True
        else:
            self.progress = False

        #Plot first time index of data
        fig,ax,p,update = cylinder_figure(self, time_idx=time_idx)


        #Animate the figure through time if required
        if animate:
            frames = int(len(time))
            self.ani = anim.FuncAnimation(fig, update, frames=frames, interval=10, blit=False, repeat=True)
            print('\nAnimating...')

            if save:
                #Save the animation as a movie if needed
                print('Saving file '+movie_filename+' at '+str(dpi)+'dpi and '+str(fps)+'fps')
                self.ani.save(movie_filename,dpi=dpi,fps=fps)
                print('\nSAVED')

            else:
                plt.show()

        elif save:
            print('Saving file '+image_filename+' at '+str(dpi)+'dpi')
            plt.savefig(image_filename,dpi=dpi)
            print('\nSAVED')

        else:
            plt.show()

    #################################

    def plot_cylinders_3D(self, animate=False, save=False, time_idx=0):

        '''
        Method for plotting flow as 3D concentric cylinders e.g. for torsional oscillations

        Keyword arguments:

            'animate' - bool. If True will animate the plot (default: False)
            'save'    - bool. If True the plot will be saved rather than plotted (default: False)

        '''


        #Load in variables from self
        data = self.data
        time = self.time
        radius = self.radius

        speed = self.speed

        movie_filename = self.movie_filename
        image_filename = self.image_filename
        dpi=self.dpi
        fps=self.fps


        if save and animate:
            self.progress = True
        else:
            self.progress = False


        #Plot first time index of data
        fig,ax,cylinders,(texture_funcs,texture_plots,texture_theta),update = cylinder_3D_figure(self, time_idx=time_idx)

        #Animate the figure through time if required
        if animate:
            frames = int(len(time))
            self.ani = anim.FuncAnimation(fig, update, frames=frames, interval=10, blit=False, repeat=True)
            print('\nAnimating...')

            if save:
                #Save the animation as a movie if needed
                print('Saving file '+movie_filename+' at '+str(dpi)+'dpi and '+str(fps)+'fps')
                self.ani.save(movie_filename,dpi=dpi,fps=fps)
                print('\nSAVED')

            else:
                plt.show()

        elif save:
            print('Saving file '+image_filename+' at '+str(dpi)+'dpi')
            plt.savefig(image_filename,dpi=dpi)
            print('\nSAVED')

        else:
            plt.show()

    #################################

    def plot_contours(self,animate=False,save=False, time_idx=0):

        '''
        Method for plotting flow with filled contours.

        Keyword arguments:

            'animate' - bool. If True will animate the plot, default: False
            'save'    - bool. If True the plot will be saved rather than plotted  default: False

        '''


        #Load in variables from self
        data = self.data
        time = self.time
        radius = self.radius
        theta = self.theta

        speed = self.speed

        movie_filename = self.movie_filename
        image_filename = self.image_filename
        dpi=self.dpi
        fps=self.fps


        #Check if progress needs to be written to screen for saving
        if save:
            self.progress = True
        else:
            self.progress = False


        #Set up and plot the first figure
        fig,ax,p,levels,update = contour_figure(None, self, None, setup=True, time_idx=time_idx)



        #Animate the figure if needed
        if animate:
            frames = int(len(time))
            self.ani = anim.FuncAnimation(fig, update, frames=frames, interval=10, blit=False, repeat=True)

            print('\nAnimating...')

            #Save the animation into a movie if needed
            if save:

                print('Saving file '+movie_filename+' at '+str(dpi)+'dpi and '+str(fps)+'fps')
                self.ani.save(movie_filename)
                print('\nSAVED')

            else:
                plt.show()


        #Save the plot as a picture if needed
        elif save:
            print('Saving file '+image_filename+' at '+str(dpi)+'dpi')
            plt.savefig(image_filename,dpi=dpi)
            print('\nSAVED')

        #Plot the figure if not animating or saving
        else:
            plt.show()

########################################################################################


#Extra functions required
########################################################################################

def make_cylinders(ax,n):
    #Make stacked circles representing cylinders.
    r = np.linspace(1,0,n+1)[:-1]
    cylinders = []
    for i in range(n):
        cylinders.append(plt.Circle([0,0],radius=r[i],ec='k', transform=ax.transData._b))

    return cylinders

def make_cylinder_3D(radius,aspect_ratio,height):

    a = radius
    b = a/aspect_ratio

    h1, h2 = height

    theta = np.linspace(np.pi/2, 5*np.pi/2,40)
    x = a*np.sin(theta)
    y = b*np.cos(theta) + h2

    x = np.append(x,[a,a])
    y = np.append(y,[h2,h1])

    theta = np.linspace(np.pi/2, 3*np.pi/2,20)
    for i in range(theta.size):
        x = np.append(x,a*np.sin(theta[i]))
        y = np.append(y,b*np.cos(theta[i]) + h1)

    x = np.append(x,[-a,-a])
    y = np.append(y,[h1,h2])

    return x,y

def create_texture_func(theta,a,b,height):

    def func(theta):
        x = a*np.sin(theta)
        y = b*np.cos(theta) + height
        return x, y

    return func

def setup_polar_fig():
    #Set up a figure in polar co-ordinates
    fig, ax = plt.subplots(1,1,subplot_kw=dict(projection='polar'))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_theta_offset(0.5*np.pi)
    ax.set_theta_direction('clockwise')
    ax.set_ylim([0,1])

    return fig, ax

def contour_figure(ax,flow_class,levels,setup=False,time_idx=0):

    #Set up the figure for contour plotting the data

    #Read in variables from flow_class
    data = flow_class.data
    radius = flow_class.radius
    theta = flow_class.theta
    time = flow_class.time

    speed = flow_class.speed
    progress = flow_class.progress

    title = flow_class.title
    colorbar_title = flow_class.colorbar_title

    c_scale = flow_class.c_scale


    if setup:


        # Create the figure and axes
        fig, ax = setup_polar_fig()

        #Set min/max data values for colorbar (such that it is symmetric)
        levels = np.linspace(-c_scale,c_scale,60) #Contour levels

        #Plot the first figure
        p = [contour_figure(ax,flow_class,levels,time_idx=time_idx)]
        ax.autoscale(False)

        c_ticks = np.linspace(levels[0],levels[-1],5) #Tick values for colourbar.

        cbar = plt.colorbar(p[0][0],ax=ax, ticks=c_ticks)
        cbar.ax.set_title(colorbar_title,y=1.1)
        pos = cbar.ax.get_position()
        cbar.ax.set_position([pos.x0+0.05,pos.y0*2,pos.width,pos.height/2])

        ########
        def update(i):
            #Update function for animation


            #print progess if saving.
            if progress:
                text='\rSaving frame '+str(i+1)+'/'+str(data.shape[2])
                sys.stdout.write(text)
                sys.stdout.flush()

            #Remove the existing contours
            for tp in p[0][0].collections:
                tp.remove()

            #Update the plot
            p[0] = contour_figure(ax,flow_class,levels,time_idx=i)
            plt.title(title % time[i])

            return p
        #########


        return fig,ax,p,levels,update

    else:


        #Grid radius and theta
        THETA, R = np.meshgrid(theta,radius)

        #Plot the contours
        return [ax.contourf(THETA,R,data[:,:,time_idx],levels,cmap='jet')]

def cylinder_figure(flow_class, time_idx=0):


    #Read in variables from flow_class
    data = flow_class.data
    radius = flow_class.radius
    time = flow_class.time

    speed = flow_class.speed
    progress = flow_class.progress

    title = flow_class.title
    colorbar_title = flow_class.colorbar_title

    c_scale = flow_class.c_scale



    # Create the figure and axes
    fig, ax = setup_polar_fig()

    n_cylinders = radius.size-1

    # Create cylinders
    cylinders = make_cylinders(ax,n_cylinders)
    for c in cylinders:
        ax.add_artist(c)
    p = [cylinders]

    #Set min/max data values for colorbar (such that it is symmetric)
    levels = np.linspace(-c_scale,c_scale,60) #Contour levels

    # Create colorbar based on data range
    cmap = plt.cm.get_cmap('jet')
    c_ticks = np.linspace(levels[0],levels[-1],5) #Tick values for colourbar.
    ax.autoscale(False)

    norm = matplotlib.colors.Normalize(vmin=-c_scale, vmax=c_scale)
    sm = matplotlib.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm,ticks=c_ticks)
    cbar.ax.set_title(colorbar_title,y=1.1)
    pos = cbar.ax.get_position()
    cbar.ax.set_position([pos.x0+0.05,pos.y0*2,pos.width,pos.height/2])


    # Set colours of cylinders
    for j,c in enumerate(p[0]):
            j = data.shape[0]-(j+2) #so that j corresponds to direction the data iterates
            c.set_facecolor(cmap(0.5*(1+((data[j+1,0,time_idx]+data[j,0,time_idx])/2)/c_scale))[:-1])




    #Create dots at the center radii of the cyclinders
    r  = np.zeros(0)
    th = np.zeros(0)
    for i in range(n_cylinders):
        r_cyl = (radius[i]+radius[i+1])/2
        n_dots = np.max([2,2*(i+1) - 1])
        r  = np.append(r,r_cyl*np.ones(n_dots))
        th = np.append(th,np.linspace(0,2*np.pi,n_dots+1)[:-1])

    texture = np.column_stack((r,th))

    p.append(ax.plot(texture[:,1],texture[:,0],'ko',markersize=3))



    # Define the update function for animation
    ########
    def update(i):

        #print progess to screen if saving every 10 frames
        if progress:
            text='\rSaving frame '+str(i+1)+'/'+str(data.shape[2])
            sys.stdout.write(text)
            sys.stdout.flush()

        cmap = plt.cm.get_cmap('jet')

        #Set colors of circles by data
        for j,c in enumerate(p[0]):
            j = data.shape[0]-(j+2) #circles iterate from outside in, whereas data iterates inside out
            c.set_facecolor(cmap(0.5*(1+((data[j+1,0,i]+data[j,0,i])/2)/c_scale))[:-1])


        plt.title(title % time[i])

        #Advect the texture
        factor = 100
        texture[:,1] = texture[:,1] - np.interp(texture[:,0],radius,data[:,0,i])*speed/factor
        p[-1][0].set_data(texture[:,1],texture[:,0])


        return p
    #########




    return fig,ax,p,update

def cylinder_3D_figure(flow_class, time_idx=0):


    #Read in variables from flow_class
    data = flow_class.data
    radius = flow_class.radius
    time = flow_class.time

    speed = flow_class.speed
    progress = flow_class.progress

    title = flow_class.title
    colorbar_title = flow_class.colorbar_title

    c_scale = flow_class.c_scale

    # Create the figure and axes
    fig, ax = plt.subplots()
    plt.axis('off')
    plt.axis('square')
    ax.grid(False)
    plt.xlim(-1.01,1.1)
    plt.ylim(-1,1.4)
    # ax.set_position([-0.6,-0.15,1.5,1.3])

    #####################
    #Create cylinders
    #####################

    #Number
    n_cylinders = radius.size-1

    #Set properties of cylinders (heights shifted slightly)
    aspect_ratio = 1.5
    radius = np.linspace(0,1,n_cylinders+1)
    heights = np.sqrt(1-radius**2)
    shift = 0.3 #vertical shift in y axis to lower half to make more spherical
    #Plot bottom half of sphere, setting plot order
    order = 1
    top,bottom = [],[]
    for i in range(1,n_cylinders+1):
        x,y = make_cylinder_3D(radius[i],aspect_ratio,(-heights[i-1]+shift,0+shift))
        bottom.append(plt.gca().add_patch(plt.Polygon(np.column_stack((x,y)),zorder=order)))
        order += 1
        plt.plot(x,y,'-k',lw=1,zorder=order)#plot edges
        order += 1


    #Swap order of cylinder plotting for top half
    radius = radius[::-1]
    heights = heights[::-1]
    heights[0] = -heights[1]+shift

    #Initialise lists for texture function and plotted line objects and anglular position (theta)
    texture_funcs = []
    texture_plots = []
    texture_theta = []
    #Plot top half of cylinders and texture points in correct order
    for i in range(n_cylinders):
        x,y = make_cylinder_3D(radius[i],aspect_ratio,(heights[i],heights[i+1]))
        top.append(plt.gca().add_patch(plt.Polygon(np.column_stack((x,y)),zorder=order)))
        order += 1
        plt.plot(x,y,'-k',lw=1,zorder=order)#plot edges
        order += 1

        #scale texture points (x,y) to lie on top of cylinders
        scale = (radius[i] - (radius[i]-radius[i+1])/2)

        #Create a function that generates (x,y) for each cylinders texture points.
        n_dots = (2*n_cylinders -1) - i*2
        n_dots = np.max([2,n_dots])
        texture_theta.append(np.linspace(0,2*np.pi,n_dots+1)[:-1])
        texture_funcs.append(create_texture_func(texture_theta[-1],scale,scale/aspect_ratio,heights[i+1]+0.01))

        #plot texture points
        x_t, y_t = texture_funcs[-1](texture_theta[-1])
        texture_plots.append(plt.plot(x_t,y_t,'ok',markersize=2.3,zorder=order))
        order += 1


    #Set min/max data values for colorbar (such that it is symmetric)
    levels = np.linspace(-c_scale,c_scale,60) #Contour levels

    # Create colorbar based on data range
    cmap = plt.cm.get_cmap('jet')
    c_ticks = np.linspace(levels[0],levels[-1],5) #Tick values for colourbar.
    ax.autoscale(False)

    norm = matplotlib.colors.Normalize(vmin=-c_scale, vmax=c_scale)
    sm = matplotlib.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm,ticks=c_ticks)
    cbar.ax.set_title(colorbar_title,y=1.1)
    pos = cbar.ax.get_position()
    cbar.ax.set_position([pos.x0+0.05,pos.y0*2,pos.width,pos.height/2])



    #Create list of cylinders and set colour
    cylinders = []
    for i in range(n_cylinders):
        cylinders.append([top[i],bottom[-i -1]])
        for c in cylinders[-1]:
            c.set_facecolor(cmap(0.5*(1+((data[i+1,0,time_idx]+data[i,0,time_idx])/2)/c_scale))[:-1])



    #So they iterate inside out, same as data
    cylinders = cylinders[::-1]
    texture_funcs = texture_funcs[::-1]
    texture_plots = texture_plots[::-1]
    texture_theta = np.flipud(texture_theta)


    # Define the update function for animation
    ########
    def update(i):

        #print progess to screen if saving, every 10 frames
        if progress:
            text='\rSaving frame '+str(i+1)+'/'+str(data.shape[2])
            sys.stdout.write(text)
            sys.stdout.flush()

        cmap = plt.cm.get_cmap('jet')

        #Set colors of cylinders by data and advect texture
        for j in range(len(cylinders)):
            for c in cylinders[j]:
                c.set_facecolor(cmap(0.5*(1+((data[j+1,0,i]+data[j,0,i])/2)/c_scale))[:-1])

            factor = 100
            texture_theta[j][:] += -((data[j+1,0,i]+data[j,0,i])/2)*speed/factor
            x_t, y_t = texture_funcs[j](texture_theta[j])
            texture_plots[j][0].set_data(x_t,y_t)

        plt.title(title % time[i])
    #########




    return fig,ax,cylinders,[texture_funcs,texture_plots,texture_theta],update
