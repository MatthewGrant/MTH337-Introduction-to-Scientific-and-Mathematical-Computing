
# coding: utf-8

# ### Matthew Grant
# ### MTH 337
# ### Report 9: Global Positioning System (Multivariable Optimization)

# In[137]:

#%pylab 
from pylab import *
from numpy import * 


# In[3]:

def myfx(x):
    return (x[0]-5)**2 + (x[1]-3)**2 + 17


# In[12]:

def stumbleDown(p,stepsize,tol=.1,steps=100):
    
    fail = 0 
    i = 0 
    #for i in range(steps):
    while i < 100 or stepsize > tol:    
        # 1d array ([x,y]) between [-stepsize,stepsize]
        step = stepsize*(2*random.rand(2)- 1)                
        q = array(p) + step 
        
        if myfx(q) < myfx(p):
            plot([p[0],q[0]],[p[1],q[1]],'g')
            p = q 
            fail = 0 
            i += 1 
            print 'step',i,"F(q):",myfx(q),"F(p):",myfx(p),'True',"x,y",p
            
        else: #F(q) > F(p)
            plot([p[0],q[0]],[p[1],q[1]],'r')
            q = array(p) + step 
            fail += 1
            i += 1
            print 'step',i,"F(q):",myfx(q),"F(p):",myfx(p),'False',"x,y",p  # "{:<4d} {:11s} {:4.3f} {} [:5.3f]".format(i,str(),...)
            
        if fail >= 10:
            stepsize = stepsize/2.
      


# In[43]:

stumbleDown([1,1],.5);


# In[151]:

def totalError(x,sats=sats,dists=dists):
    ''' arguments: (sats) 2D array of (x,y) satellite locations
                   (dists) 1D array of distances from each satellite to point (reciever)
                   (x) (xi,yi) tuple of changing guesses 
    '''

    # Data 
    # distance from each satellite to point
    dists = array([251.6,397,270.5,222.6]) 

    # location of each satellite from a common reference point 
    sats = array([ 
         [412.5,257.7],
         [580.0,876.0],
         [438.9,750.0],
         [359.2,658.8],
         ])

    return sum(array([(sqrt((sats[:,0,newaxis]-x[0])**2 + (sats[:,1,newaxis]-x[1])**2) - dists[:, newaxis])**2]))
    #return sum((hypot(sats[:, 0, numpy.newaxis]-x[0], sats[:, 1, numpy.newaxis]-x[1]) - dists[:,newaxis])**2)
   


# In[161]:

def stumbleDown2D(p,stepsize,tol=10e-8):
    '''Direct Search - Minimizes the total error of the objective function by taking random steps.

    Parameters
    ----------
    p : array_like
        1-D array representing the coordinates of an inital guess.
    stepsize : float
        The inital amount that the algorithm moves at each step
    tol : float
        stopping crieteria for the while loop. 
    '''
    fail = 0 
    i = 0
    
    while stepsize > tol:    
        # 1d array ([x,y]) between [-stepsize,stepsize]
        step = stepsize*(2*random.rand(2)- 1) 
        
        # Take a random step 
        q = array(p) + step 
        
        # Compare the previous step with the current step 
        if totalError(q) < totalError(p):
            plot([p[0],q[0]],[p[1],q[1]],'g')
            p = q 
            
            # Increment counters 
            fail = 0 
            i += 1 
            
            print 'step',i,"F(q):",myfx(q),"F(p):",myfx(p),'True',"x,y",p
            
        else: 
            plot([p[0],q[0]],[p[1],q[1]],'r')
            title('Steps to find optimal GPS location')
            xlabel('x location (cm)')
            ylabel('y location (cm)')
            legend()
            
            # Take another rendom step 
            q = array(p) + step 
            
            #Increment counters 
            fail += 1
            i += 1
            
            print 'step',i,"F(q):",myfx(q),"F(p):",myfx(p),'False',"x,y",p 
            
        if fail >= 10:
            # Changes step size after 10 failures 
            stepsize = stepsize/2.
             


# In[163]:

stumbleD own2D(array([280,350]),50)


# In[ ]:



