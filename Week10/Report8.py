# ### Matthew Grant
# ### MTH 337
# ### Report 8: The Generation and Use of Random Numbers
# 

# In[2]:

#%pylab 
style.use('ggplot')
from numpy import *


# ### Exercise 1
# * Test the linear congruential generators in your rng and randu functions, and the generator in random.rand for (i) uniformity, and (ii) lack of (coarse-scale) successive pair correlation.

# In[12]:

#EX 1: Random Number Generator 
def rng(seed, npts):
    a=427419669081
    m=999999999989
    result = []
    x = seed
    for i in xrange(npts):
        x = (a*x)%m
        result.append(x)
    results = array(result)
    
    return (float(x)/m)*results    


# In[117]:

r1 = rng(40,100000)
hist(r1,bins=50);
title('Random number generator');


# In[122]:

r2 = rng(40,10000)
plot(r2[:-1], r2[1:], 'b.', ms=2.5, alpha=.7)
title('RNG - Pair Wise Correlation');


# In[8]:

#RANDU, linear congruential number generator 
def randu(seed, npts):
    a=2**16 + 3
    m=2**31
    result = []
    x = seed
    for i in xrange(npts):
        x = (a*x+1)%m
        result.append(x)
    results = array(result)
    return (float(x)/m)*results


# In[123]:

randu1 = randu(40,100000)
hist(randu1,bins=50)
title('RANDU RNG');


# In[125]:

randu2 = randu(40,10000)
plot(randu2[:-1], randu2[1:], 'b.', ms=2.5, alpha=.7)
title('RANDU - Pairwise Correlation');


# In[126]:

rr = random.rand(100000)
hist(rr, bins=50)
title('Random.rand');


# In[127]:

rr2 = random.rand(10000)
plot(rr2[:-1], rr2[1:], 'b.', ms=2.5, alpha=.7)
title('random.rand Pair Wise Correlation');


# ### EX 2
# 1. Use Monte Carlo integration to average the function mysteryf in the mystery module by random sampling using numpy.random.rand over the interval [0, 5]. use numpy array operations to apply the mystery function f to all points xi and then use mean() use lots of point to get a good estimate. 
# 

# In[3]:

from mystery import mysteryf


# In[49]:

mysteryf(array([0,1,2,3,4,5]))


# In[44]:

trails = 10000
results = empty([trails])
for i in xrange(npts):
    u = random.rand(100)*5 #array of size 100 in range (0->5)
    d = mysteryf(u).mean() # mean of that 
    results[i] = d

print "Average output of Mystery Function: ",mean(results)
hist(results, bins=50);
title('Mystery Function Average Output')



# ### Ex 3
# 1. Use Monte Carlo integration to estimate the area of the "flower", whose boundary has the equation r(θ) = 2 + cos(7θ) in polar coordinates.

# In[71]:

# random number (-3 to 3) 
npts = 3000
xpts = random.rand(npts)*6-3 #(-3 to 3)
ypts = random.rand(npts)*6-3 #(-3 to 3)

# convert random points to polar coords
R = (sqrt(xpts**2 + ypts**2)) #distance 
Theta = arctan2(ypts,xpts) #angle

# Plot of the flower
theta = linspace(0, 2*pi, npts)
r = 2 + cos(7*theta)
polar(theta, r,'c',lw=2)

# plot our box of random points 
polar(Theta,R,'r.') 

# number of points inside "flower" / total points in box)
inside = R < (2 + cos(7*theta))
print "Area of Flower: ", mean(inside)
print sum(inside)/float(npts)


# ### Ex 4
# 1. Numerically estimate the probability of getting 29 hits in 100 swings in a baseball game if the probability of getting a hit on any one swing in 0.29 (and is independent of other swings).

# In[73]:

# number of trials 
n = 1000

# Generate a 2D array of shape (n, 100)
swings = random.rand(n,100)
hits = swings < 0.29 # [T,F] array should expect to have avg hits 29 or less
totals = sum(hits, axis=1) #counts the number of hits in every row (axis=1)
print "Probability of getting 29 hits out of 100 swings:", mean(totals == 29) 


# ### Ex 5  
# 1. Produce a histogram of the sums of pairs of uniformly distributed random numbers produced by random.rand.
# 2. Produce histograms for the sums of M-tuples of uniform random numbers for values of M greater than 2
# 3. See if it is possible to shift and stretch the sums of M-tuples so that their distribution converges to something as M increases without bounds.
# 4. Plot and analyze the sums of M-tuples of non-uniform random numbers.

# In[92]:

# 1
npts = 100000
m=2
a = random.rand(npts,m) 
b = sum(a,axis=1) 

hist(b/float(m), bins=50, label=str(m))
title('Sum of pairs of Uniformly Distributed Random Numbers')
legend();


# In[96]:

2#
npts = 10000
for m in xrange(2,9):
    a = random.rand(npts,m) 
    b = sum(a,axis=1) 
    hist((b)/float(m), bins=50, histtype='step', normed=True, label=str(m))
    title('Sum of M-pairs of Uniformly Distributed Random Numbers')
    legend()


# In[97]:

#3 - shift and stretch the sums of M-tuples so that their distribution converges 
# to something as M increases without bounds.????
npts = 10000
for m in xrange(3,12):
    a = random.rand(npts,m) 
    b = sum(a,axis=1) 
    hist((b-m/2.)/float(log(m)), bins=50,normed=True, histtype='step', label=str(m)) #b-m/2.0 centers about 0. 
title('Convergence of M-pairs of Uniformly Distrubuted Random Numbers')
legend()


# In[107]:

#4 - Plot and analyze the sums of M-tuples of non-uniform random numbers.??
npts = 10000
for m in xrange(3,12):
    a = random.rand(npts,m) 
    v = 2*a**(1./3.) #new random variable that has a particular pdf 
    b = sum(v,axis=1) 
    hist(v, bins=50, histtype='step', label=str(m)) #b.m/2.0 centers about 0. 
legend()


# ### Ex 6
# 1. Implement the simple stock market model defined in class. Use a value for μ of 0.0 and σ of 5% to find out what happens to an initial investment of 1 unit of money over 365 steps.
#     * μ (m) = Rate of growth
#     * e = "Stochatic" component
#     * sigma - Volatility 
# 
# 2. Plot the changing price of several stocks over this period.
# 3. Plot a histogram of final stock prices after 365 steps using a large number of trials.
# 4. Estimate the "expected value" (average over all trials) of the investment after 1 year.
# 5. Calculate the likelihood of losing money.
# 6. Calculate the "most likely" value of the investment after 1 year, using an appropriate definition of "most likely".
# 7. Draw some conclusions about investing, or on the value of money.
# 8. Run another simulation using a more modest value for σ of 1%.

# In[110]:

# 1 - implement simple stock market model 
steps = 365
s = 1
m = 0.0 # 
sigma = .05 # 
results = []

for i in range(steps):
    e = random.normal() 
    s *= (1 + m + sigma*e)
    results.append(s)
plot(results, label=str(1))
title('Stock Market Simulation');


# In[116]:

#2 changing price of Several Stocks (500)
steps = 365
s = 1
m = 0.0
sigma = .05
stocks = 500
results = empty([steps,stocks])

for i in range(steps):
    e = random.normal(size=stocks) #add size 
    s *= (1 + m + sigma*e)
    results[i] = s
plot(results)
title('Stock Market Simulation of 500 Stocks');


# In[119]:

#3 - histogram

hist(results[-1], bins=20)
xlabel('return')
ylabel('number of stocks')
title('Stock Market Simulation');


# In[69]:

#4 - Estimate the "expected value" (average over all trials) of the investment after 1 year.
print "Average Expected Value after 1 year", mean(results)


# In[70]:

#5 - Calculate the likelihood of losing money.
loss = results[-1] < 1 # [T,F] array of size 500
total = sum(loss) # number of True cases (stocks whose final values are less than 1)
print "Likelihood of loosing money: ", (total/float(results.shape[1]))*100, "Percent"


# In[71]:

#6 - Calculate the "most likely" value of the investment after 1 year
print "Typical value of investments after 1 year", mean(results[-1])


# In[33]:

#7 - Draw some conclusions about investing
# It's a risky venture!


# In[123]:

#8 - Run another simulation using a more modest value for σ of 1%. (increased volatility)

steps = 365
s = 1
m = 0.0
sigma = .10
stocks = 500
results = empty([steps,stocks])

for i in range(steps):
    e = random.normal(size=stocks) #add size 
    s *= (1 + m + sigma*e)
    results[i] = s
plot(results)
title('Stock market simulation of 500 stocks with increase volatility')

#Calculate the likelihood of losing money (increase sigma = .1, volitility)
loss = results[-1] < 1 # [T,F] array of size 500
total = sum(loss) # number of True cases (stocks whose final values are less than 1)
print "Likelihood of loosing money: ", total/float(results.shape[1])

#Calculate the "most likely" value of the investment after 1 year
print "Typical investments after 1 year", mean(results)


# In[124]:

hist(results[-1], bins=20)
xlabel('return')
ylabel('number of stocks');
title('Stock market simulation of 500 stocks with increase volatility')


# Incresed volitility (sigma) equals a greater chance to loose money with a lower return on investment. 
