from math import *
def f(x):
    return x*cos(x)-x**2*sin(x)
def f1(x):
    return (1-x**2)*cos(x)-3*x*sin(x)
h=0.001
x=3.0
# for i in range(12):
f1_simetrik=(f(x+h)-f(x-h))/(2*h)
f1_ileri=(f(x+h)-f(x))/h
f1_geri=(f(x)-f(x-h))/h
f1_tam=f1(x)
fark1=f1_tam-f1_simetrik
fark2=f1_tam-f1_ileri
fark3=f1_tam-f1_geri
print("%.6f" % h,"%.10f" % fark1,"%.10f" % fark2,"%.10f" % fark3)
#h=h/10.0
