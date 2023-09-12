from math import *
from numpy import *
def f(x): return x*exp(x)
h=0.2
x0=2.0
iMax=4
# No change required after this line
###################################################################
def dfunc(f,x,i,h):
        if i==1:
                out=( f(x+h)-f(x-h))/(2*h)
        else:
                out = dfunc(f,x,i-1,h)-((dfunc(f,x,i-1,2*h)-dfunc(f,x,i-1,h))/(2**(2*(i-1))-1.0))
        return out
print '{0:<4s} {1:^12s} {2:^12s} {3:^12s} {4:^12s}'.format('h','D1','D2','D3','D4')

for i in range(1,iMax+1):
        print 'h:',format(h,'4.3f'),
        #print '{0:4.3f}'.format(h),
        for j in range(1,i+1):
                p=dfunc(f,x0,j,h)
                #print 'D'+str(j)+'= ', format(p,'9.6f'),
                #print '{h:3.2f} D{order!s:s}={approx:9.6f}'.format(h=h,order=j,approx=p),
                print '{:12.9f}'.format(p),
        print  
        h=h/2.0
