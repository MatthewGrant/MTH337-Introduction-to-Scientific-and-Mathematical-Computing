# ### Matt Grant
# ### MTH 337
# ### Report 4: Floating Point Numbers


from pylab import *
from numpy import *
style.use('ggplot')
import sys

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})


# In[2]:

data = loadtxt("balloon.dat", skiprows=138)

# In[3]:

minutes = data[:,0]
minutes


# In[4]:

seconds = data[:,1]
seconds


# In[5]:

temp = data[:,5]
temp


# In[6]:

time = minutes + seconds/60.0
time


# In[30]:

pressure = data[:,4]
pressure


# In[33]:

plot(time,temp ,'c.',ms=5)
xlabel('Time (minutes)')
ylabel('Temperature (C)')
title('Balloon Launch')
savefig('fig1.svg', dpi = 300)


# In[32]:

plot(time,pressure ,'r.',ms=5)
xlabel('Time (minutes)')
ylabel('Pressure (hPa)')
title('Balloon Launch')
savefig('fig2.svg', dpi = 300)


# ##Part 2: Finding the Parameters of Python Floating-Point
# 
# * The "machine epsilon" (the smallest number that, when added to 1, gives a result greater than 1).
#     (This is the spacing between 1 and the next larger #) 
# 
# * The largest floating point number that can be represented in Python.
# 
# * The smallest floating point number that can be represented in Python.
# 
# * The number of bits reserved for the mantissa (m)
# 
# * The number of bits reserved for the exponent(e)
# 
# * The bias used for the exponent(b)
# 
# * Is denormalization used?

# In[19]:

def find_epsilon():
    '''Function to find machine Epsilon'''
    m = 0
    x = 1
    while (1.0 + x) > 1.0:  
        m+=1
        x = pow(2,-m)
    print "Number of Bits for Mantissa(M):",m-1,"\nMachine Epsilon:", pow(2,-(m-1))


# In[20]:

# 52 Bits of precision
find_epsilon() 


# In[59]:

# Actual machine Epsilon
print "Actual machine Epsilon check:",sys.float_info.epsilon


# In[43]:

def smallestPossible():
    '''Function to find the smallest possible floating point number'''  
    m = 52
    b = 0
    #x = 2**(1-m-b)
    x = 1 #pow(2,1-m-b)
    while x > 0: 
        b += 1
        x = pow(2,1-m-b) #x = 2**(1-m-b)
    return "Bias:",b-1, "Smallest Number:", pow(2,(1-m-(b-1)))


# In[44]:

# Smallest Normalized number 
smallestPossible()


# In[47]:

#smallest floating point number 
print "Samllest Float check:",
sys.float_info.min


# In[60]:

#smallest denormalized number
print "Smallest denormalized float check:"
sys.float_info.min*sys.float_info.epsilon


# In[57]:

def largestPossible():
    '''Function to find the larget possible floating point number'''  
    m = 52 
    b = 1023 
    k = 0
    x = 1

    while x > 0: 
        try: 
            k += 1
            #x = (2-2**-m)*2**k  (2-2^-53)(2^1023)
            x = (2 - pow(2,-m)) * pow(2,k)
        except: 
            print "Largest floating point number:"
            return (2-2**-m)*2**(k-1)


# In[58]:

largestPossible()


# In[61]:

#Largest floating point number 
print "Smallest Float check:",
sys.float_info.max




