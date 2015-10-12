# ### MTH 337
# ### Report 6: The Butterfly Bffect
# ### Matthew Grant
# 
# ### Tasks
# 

#get_ipython().magic(u'pylab')
from pylab import *
from numpy import *
style.use('ggplot')
import matplotlib.patches as mpatches

# In[5]:

def plot_Separation(x,b,t):
    ''' Function in which seperation of similar mayfly models are plotted over time.  
    x, population as percent of max, 
    b, ratio of surviving offspring to females, 
    t, Generations'''
    
    # 2 Similar Trajectories
    delta = 1e-5
    x2 = x + delta
    
    # Loop over mayfly equations for each trajectory up to time (t) 
    for i in range(t):
           
        x = b*(1-x)*x
        x2 = b*(1-x2)*x2
        st = abs(x2-x)
        
        figure(b)
        #ylim(0,1)
        semilogy(i,st,'c.') 
        title('Semilogy Separation of Similar trajectories over Time')
        xlabel('Time')
        ylabel('Seperation of Trajectories')
        patch = mpatches.Patch(color='c', label='Growth Rate b: %s'%b)
        legend(handles=[patch])


# In[31]:

plot_Separation(.5,1.5,20)


# In[36]:

plot_Separation(.5,3.6,25)


# In[34]:

plot_Separation(.5,4,15)


# In[88]:

def separation(x,b,t):
    # 2 Similar Trajectories (x,x2)
    delta = 1e-5
    x2 = x + delta
    
    # Empty Lists 
    xList = []
    yList = []
    
    # Loop over mayfly equations for each trajectory up to time (t) 
    for i in range(t):
        # population equations    
        x = b*(1-x)*x
        x2 = b*(1-x2)*x2
        
        # log of separation values 
        st = abs(x-x2) 
        logst = log(st)
        
        # Add values to lists 
        yList.append(logst) 
        xList.append(i)
        
    #Create array from the list 
    xarray = array(xList)
    yarray = array(yList)
    
    return (xarray,yarray) 


# In[89]:

b1 = separation(.5,1.5,20) 
b1


# In[90]:

b3 = separation(.5,3.6,25)
b3


# In[91]:

b4 = separation(.5,4.0,15)
b4


# In[92]:

def best_fit((xarray,yarray),b,t, x=.5):
    ''' Function that takes two arrays and returns the best fit line '''
    
    x2 = x + 1e-5
   
    # Averages 
    xMean = mean(xarray)
    yMean = mean(yarray)
    xyMean = mean(xarray*yarray)
    xSquaredMean = mean(xarray**2)
    
    #Beta (slope) where x = t and y = logst 
    beta = ((xyMean - xMean*yMean)/(xSquaredMean - (xMean)**2))
    
    #Alpha (intercept)
    alpha = yMean - xMean*beta
    
    # Best fit line 
    bestFit = alpha + beta*xarray
    
    for i in range(t):
        x = b*(1-x)*x
        x2 = b*(1-x2)*x2
        st = abs(x2-x)
        
        # Plot figures 
        figure(b+4)
        #ylim(0,1)
        semilogy(i,st,'c.' ,label='Original Data')
        
    semilogy(xarray,exp(bestFit),'r',label='Fitted Line')
    title('Seperation of Similar Mayfly Populations over Time')
    xlabel('Time')
    ylabel('Seperation of Trajectories')
    patch = mpatches.Patch(color='c', label='Growth Rate b: %s'%b)
    legend(handles=[patch])
    
    return alpha,beta, bestFit


# In[93]:

best_fit(b1,1.5,20)


# In[81]:

best_fit(b4,4,15)


# In[94]:

best_fit(b3,3.6,25)


# In[ ]:



