from pylab import *
from numpy import *
def f(x,v,t):
    m=68.1
    g=9.8
    c=12.5
    return m*g-c*v
n=300
m=68.1
h=25.00/float(n)
t=zeros(n,float)
x=zeros(n,float)
v=zeros(n,float)
v[0]=0.0
for i in range (1,n):
    t[i]=h*i
    x[i]=x[i-1]+v[i-1]*h
    v[i]=v[i-1]+f(x[i-1],v[i-1],t[i-1])/m*h
plot(t,v,"k--")
xlabel("t")
ylabel("v")
show()

