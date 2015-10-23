
# coding: utf-8

# ### MTH 337
# ### Report6:  Simulate the dynamics of the Kepler 453b system
# ### Matthew Grant 

# In[47]:

get_ipython().magic(u'pylab')
from matplotlib import animation
style.use('ggplot')
import matplotlib.patches as mpatches


# In[93]:

def diff_P(P,t): #made aware of location of suns by passing time? 
    ''' Find DE of planet and binary suns. Assume p is 1D numpy array'''
    
    #Star 1 and 2, Mass and Distance from C.O.M.
    G = 1.0
    
    #Mass of Suns
    M1 = 0.5
    M2 = 0.5
    
    # Distance of Suns to C.O.M. 
    R1 = 0.5
    R2 = 0.5

    # Assign P a 1D array with four variables to x,y...
    x, y, vx, vy = P  #Planet: x,y position | x,y velocity
    
    # Position of Suns 
    x1 = R1*cos(t) 
    y1 = R1*sin(t)
    x2 = -R2*cos(t)
    y2 = -R2*sin(t)
    
    #Distance from Planet and each sun
    Rsun1 = (sqrt((x-x1)**2 + (y-y1)**2))**3
    Rsun2 = (sqrt((x-x2)**2 + (y-y2)**2))**3
    
    # Force on Sun 1
    ax1 = (-G*M1*(x-x1))/Rsun1
    ay1 = (-G*M1*(y-y1))/Rsun1
    
    # Force on Sun 2
    ax2 = (-G*M2*(x-x2))/Rsun2
    ay2 = (-G*M2*(y-y2))/Rsun2
    
    # Total forces
    ax = ax1 + ax2
    ay = ay1 + ay2
                            
    return array([vx,vy,ax,ay])


# In[94]:

def calculate_orbit(steps,h,x,y,vx,vy):
    
    orbit = empty((steps,4)) #2d array (steps rows, col:x,y,vx,vy)
    P = array([x,y,vx,vy]) # Initial state variables
    
    for i in xrange(steps): 
        t = i*h
        orbit[i] = P 
        Ptilde = P + h*diff_P(P,t) #[x,y,vx,vy] + h*[vx,vy,ax,ay]
        P += h*(diff_P(P,t) + diff_P(Ptilde,t+h))/2.
    return orbit


# In[178]:

def plot_orbit(steps,h,x=3.,y=0.,vx=0.,vy=.5):
    
    orbit = calculate_orbit(steps,h,x=x,y=y,vx=vx,vy=vy)
    
    #Plot Planet path
    plot(orbit[:,0],orbit[:,1],'r',ms=2)
    
    #Plot suns path
    t = linspace(0,2*pi,100)
    R1 = .5
    R2 = .5
    plot(R1*cos(t),R1*sin(t),'y',ms=2)


# In[205]:

plot_orbit(6000,.1,x=.5)


# In[210]:

# Subplots for changing x,y 
end = 5
i = 1
x =0
y = 0
#vy = 0 
figure(figsize=(10,10))
for row in range(1,end+1): 
    for col in range(1,end+1):
        subplot(end,end,i)
        plot_orbit(5000,.1, x=x,y=y,vx=0.,vy=.5)
        title('x = %s,y=%s'%(x, y))
        xticks([])
        yticks([])
        i += 1
        x += .2


# In[211]:

# Subplots for changing vy 
end = 5
i = 1
x =4
y = 0
vy = 0.4
figure(figsize=(10,10))
for row in range(1,end+1): 
    y += 0
    vy =.4
    for col in range(1,end+1):
        subplot(end,end,i)
        plot_orbit(5000,.1, x=x,y=y,vx=0.,vy=vy)
        title('x = %s,y=%s,vy=%s'%(x, y,vy))
        xticks([])
        yticks([])
        i += 1
        vy += .05



# Animation
steps = 5000
h = .1
fig, ax = subplots(figsize=(6,6))
ax.set_axis_bgcolor('k')
point, = plot([],[],'ro') #bounds point to first element in the plot return list
line, = plot([],[],'cyan')
suns, = plot([],[],'yo',ms=8)


size = 4
xlim(-size,size)
ylim(-size,size)
orbit = calculate_orbit(steps,h,x=3.,y=0,vx=0,vy=.5)


def init():
    point.set_data([],[])
    line.set_data([],[])
    # add each sun 
    suns.set_data([],[])
   
    return line, point,suns 

def animate(i):
    point.set_data(orbit[i,0], orbit[i,1]) # selects x,y data from orbit at step i
    line.set_data(orbit[:i,0], orbit[:i,1])
    # add location of each suns
    suns.set_data(sunsOrbit[:,0], sunsOrbit[:,1])
    
    return line, point,suns

animation.FuncAnimation(fig, animate,init_func=init, frames=steps, interval=20, blit=False, repeat=True)


# In[ ]:



