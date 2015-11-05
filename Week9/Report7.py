
# ### Matthew Grant
# ### MTH 337
# ### Report 7 - Newton in the complex plane

get_ipython().magic(u'pylab')
#from pylab import *
#from numpy import * 


# In[56]:

npts = 1000
x = linspace(-1,1,npts)
y = linspace(-1j,1j, npts)
X,Y = meshgrid(x,y)
# Z, array of points in the complex plane
Z = X + Y 

niters = 50
for i in range(niters):
    Z -= (Z**3 -1)/(3*Z**2)
    
r1 = complex(1,0)
r2 = complex(-.5, .5*sqrt(3))
r3 = complex(-.5, -.5*sqrt(3))

tol = 1e-6
root1 = abs(Z - r1) < tol
root2 = abs(Z - r2) < tol
root3 = abs(Z - r3) < tol

img = zeros((npts,npts,3))
img[:,:,0] = root1
img[:,:,1] = root2
img[:,:,2] = root3
imshow(img)

imsave("newton_Root.png", img)


# In[6]:

npts = 1000
x = linspace(-.01,.01,npts)
y = linspace(-.01j,.01j, npts)
X,Y = meshgrid(x,y)
# Z, array of points in the complex plane
Z = X + Y 

niters = 50
for i in range(niters):
    Z -= (Z**3 -1)/(3*Z**2)
    
r1 = complex(1,0)
r2 = complex(-.5, .5*sqrt(3))
r3 = complex(-.5, -.5*sqrt(3))  

tol = 1e-6
root1 = abs(Z - r1) < tol
root2 = abs(Z - r2) < tol
root3 = abs(Z - r3) < tol

img = zeros((npts,npts,3))
img[:,:,0] = root1
img[:,:,1] = root2
img[:,:,2] = root3

imshow(img)

imsave("newton_Root_zoom.png", img)


# Encoding number of iterations needed for root to converge 
# Inital setup
npts = 1000
x = linspace(-1,1,npts)
y = linspace(-1j,1j, npts)
X,Y = meshgrid(x,y)
# 2D array of points in the complex plane (1000,1000)
Z = X + Y 

# Our 3 possible Roots 
r1 = complex(1,0)
r2 = complex(-.5, .5*sqrt(3))
r3 = complex(-.5, -.5*sqrt(3))  

# Loop through and check for convergance
maxNiters = 40

# Need to store the number of iterations to convergance for each point? 
alpha = empty((npts,npts), dtype=int) 

#iterate 
for i in range(maxNiters):
    Z -= (Z**3 -1)/(3*Z**2)
    alpha +=  (abs(Z-r1)<tol) | (abs(Z-r2)<tol) | (abs(Z-r3) < tol)

# Normalize alpha to in range 0-1  
alpha = alpha/float(alpha.max())    

# Testing for convergance after number of iterations
tol = 1e-6
root1 = abs(Z - r1) < tol #Root 1  
root2 = abs(Z - r2) < tol #Root 2
root3 = abs(Z - r3) < tol # Root 3 

img = zeros((npts,npts,4)) 
img[:,:,0] = root1
img[:,:,1] = root2 
img[:,:,2] = root3
img[:,:,3] = alpha
imshow(img)

imsave("newton_Root_brightness.png", img)


# 4 Degree polynomial f(z) = z^4 - 1 
npts = 1000
x = linspace(-1,1,npts)
y = linspace(-1j,1j, npts)
X,Y = meshgrid(x,y)
# 2D array of points in the complex plane (1000,1000)
Z = X + Y 

# Our 4 possible Roots 
r1 = complex(1,0)
r2 = complex(-1,0)
r3 = complex(0,1)  
r4 = complex(0,-1)  

# Loop through and check for convergance
maxNiters = 50
tol = 1e-6

#iterate 
for i in range(maxNiters):
    Z = Z - ((Z**4 -1.0)/(4*Z**3))
    #alpha +=  (abs(Z-r1)<tol) | (abs(Z-r2)<tol) | (abs(Z-r3) < tol)

# Normalize alpha to between 0-1  
#alpha = alpha/float(alpha.max())    

# Testing for convergance after number of iterations

root1 = abs(Z - r1) < tol  
root2 = abs(Z - r2) < tol 
root3 = abs(Z - r3) < tol  
root4 = abs(Z - r4) < tol 

img = zeros((npts,npts,3)) 
img[root1] = [1, 0, 0]
img[root2] = [0, 1, 0]
img[root3] = [0, 0, 1]
img[root4] = [1, 1, 0]
#img[:,:,3] = root4
imshow(img)

imsave("newton_Root_4degree.png", img)


# f(z) = z^3 - z
npts = 1000
x = linspace(-1,1,npts)
y = linspace(-1j,1j, npts)
X,Y = meshgrid(x,y)
# 2D array of points in the complex plane (1000,1000)
Z = X + Y 

# Our 4 possible Roots 
r1 = complex(1,0)
r2 = complex(-1,0)
r3 = complex(0,0)  
 

# Loop through and check for convergance
maxNiters = 50
tol = 1e-6

#iterate 
for i in range(maxNiters):
    Z = Z - ((Z**3 -Z)/(3*Z**2 - 1))
    #alpha +=  (abs(Z-r1)<tol) | (abs(Z-r2)<tol) | (abs(Z-r3) < tol)

# Normalize alpha to between 0-1  
#alpha = alpha/float(alpha.max())    

# Testing for convergance after number of iterations

root1 = abs(Z - r1) < tol  
root2 = abs(Z - r2) < tol 
root3 = abs(Z - r3) < tol  

img = zeros((npts,npts,3)) 
img[root1] = [1, 0, 0]
img[root2] = [0, 1, 0]
img[root3] = [0, 0, 1]

imshow(img)


imsave("newton_Root_z3_z.png", img)

