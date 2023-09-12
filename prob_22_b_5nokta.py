from math import *
def f(x):
    return 3*x*exp(x)-cos(x)
def f2(x):
    return 3*(2+x)*exp(x)+cos(x)
h=0.001
x=1.3
# for i in range(12):
f2_simetrik=(-f(x+2*h)+16*f(x+h)-30*f(x)+16*f(x-h)-f(x-2*h))/(12*h**2)
f2_ileri=(-f(x+3*h)+4*f(x+2*h)-5*f(x+h)+2*f(x))/(h**2)
f2_geri=(2*f(x)-5*f(x-h)+4*f(x-2*h)-f(x-3*h))/(h**2)
f2_tam=f2(x)
fark1=f2_tam-f2_simetrik
fark2=f2_tam-f2_ileri
fark3=f2_tam-f2_geri
print("%.6f" % h,"%.10f" % fark1,"%.10f" % fark2,"%.10f" % fark3)
#h=h/10.0
