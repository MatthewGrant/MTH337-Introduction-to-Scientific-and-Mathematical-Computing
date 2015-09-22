
# ## MTH 337 
# ###Report 2: C-numbers
# Find C-numbers: integer n > 1 such that $b^n$ mod $n = b$ for all integers $1<b<n$

import numpy as np
print 'C-numbers up to 100,000'


# Method to determine primality through trial division 
def is_prime(n): 
    import math
    factor = 2
    isPrime = True
    upperBounds = math.sqrt(n)
    while factor <= upperBounds: 
        if n%factor == 0:
            isPrime = False
            break
        factor += 1
    return isPrime

def testFermat(p,b):
    #test using fermat theorm  
    return pow(b,p,p) == b 
    
def fermat(p,b): 
    """ function fermat(p,n) tests whether a number is prime based on Fermat's little theorem"""
    isFermatPrime = True
    for b in xrange(2,p): # iterate through b, 1 < b < p, checking with testFermat function 
        if not testFermat(p,b):
            isFermatPrime = False #not prime
            break
        else:
            isFermatPrime = True # is prime 
            b += 1
    return isFermatPrime        


print "c-numbers using list of primes"
for i in xrange(10,100000):
    if not is_prime(i) and fermat(i,2):
        print i


# Code taken from Python Cookbook 
# http://archive.oreilly.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html?page=last
import itertools
def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p
            
def get_primes_erat(n):
    return list(itertools.takewhile(lambda p: p<n, erat2()))


primes = get_primes_erat(100000)
print "list of primes up to 100000:" ,len(primes)


print "c-numbers using list of primes"
for i in xrange(10,100000):
    if i not in primes and fermat(i,2):
        print i

