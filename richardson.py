from numpy import *
from math import *

x=1
n=4
h=0.4
d1=zeros((n+1,n+1),dtype=float)

#definition of f(x) and Richardson subroutine
def f(x):
    return exp(x**2)+3*sin(sqrt(x))

def richardson(f,x,n,h):
    # d[n,n] will contain the most accurate approximation to f'(x).
    d=zeros((n+1,n+1),dtype=float)
    for i in range(n+1):
        d[i,0] = 0.5*(f(x+h)-f(x-h))/h
        powerOf4 = 1  # values of 4^j
        for j in range(1,i+1):
            powerOf4 = 4*powerOf4
            d[i,j] = d[i,j-1]+(d[i,j-1]-d[i-1,j-1])/(powerOf4-1)
        h = 0.5 * h
    return d

#print of the results
d1=richardson(f,x,n,h)
print(d1)
