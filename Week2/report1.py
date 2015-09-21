
# Matthew Grant
# MTH 337, Report 1 code

import math
import numpy as np
#get_ipython().magic(u'pylab --no-import-all')
from pylab import *


# Define method is_Square of num
def is_Square(num):
    """Returns True if num is a perfect square, A^2 + B^2 = C^2"""
    from math import sqrt
    if num == int(math.sqrt(num))*int(math.sqrt(num)): 
        return True
    else:
        return False


# Define method Geatest Common Divisor of a,b
def myGCD(a,b): 
    """Returns Greatest Common Divisor between two numbers a,b"""
    c = a%b
    while c > 0:
        #print a,b,r
        a,b,c = b,c,b%c 
    return b 


# Define method to find PPT up to n
def prime_Trips2(n): #13ms --> 100
    listA =[]        #1.1s --> 1000
    listB =[]        #26.5s --> 5000
    for a in xrange(1,n):
        a2 = a*a
        for b in xrange(a+1,n): #b>a
            c2 = a2 + b*b
            c = int(math.sqrt(a2 + b*b))
            if is_Square(c2) and myGCD(a,b) == 1:
                    listA.append(a)
                    listB.append(b)
                    #print (a,b,c)
    return zip(listA,listB)


#All pythagorean triples 
def trips(n): 
    listA =[]        
    listB =[]
    listC = []
    for a in xrange(1,n):
        a2 = a*a
        for b in xrange(a+1,n): #b>a
            c2 = a2 + b*b
            c = int(math.sqrt(a2 + b*b))
            if is_Square(c2):
                    listA.append(a)
                    listB.append(b)
                    listC.append(c)
                    #print (a,b,c)
    return zip(listA,listB)



coords_5000 = prime_Trips2(5000) 
print 'PPT up to 5000 complete'

coords_5000all = trips(5000)
print 'All PT up to 5000 complete'

# find and print number of PPT
print len(coords_5000),'Primative Triples found for a,b < 5000'

# Plot primative triples. 
x,y = zip(*coords_5000)
figure(1)
plot(x,y,'r.')
xlabel('a')
ylabel('b')
title('Primitive Pythagorean Triples (a,b <= 5000)')

# Plot symmetric primitive triples in blue.
y,x = zip(*coords_5000)
plot(x,y,'b.') 
show()

#Plot all Pythagorean Triples (a,b <= 5000)
figure(2)
x,y = zip(*coords_5000all)
plt.plot(x,y,'k.',ms=3)
y,x = zip(*coords_5000all)
plot(x,y,'k.',ms=3)
xlabel('a')
ylabel('b')
title('All Pythagorean Triples (a,b <= 5000)')
show()

# Matrix multiplication PPT ternary Tree using eulerlib package
#from eulerlib import *
#get_ipython().magic(u'pinfo eulerlib')





