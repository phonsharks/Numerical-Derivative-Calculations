from math import *
def f(x):
    return log(x)
def f2(x):
    return -1/(x**2)
h=0.1
x=1.0
for i in range(3):
    f2_simetrik=(f(x+h)-2*f(x)+f(x-h))/(h**2)
    f2_ileri=(f(x+2*h)-2*f(x+h)+f(x))/(h**2)
    f2_geri=(f(x)-2*f(x-h)+f(x-2*h))/(h**2)
    f2_tam=f2(x)
    fark1=f2_tam-f2_simetrik
    fark2=f2_tam-f2_ileri
    fark3=f2_tam-f2_geri
    print("%.6f" % h,"%.10f" % fark1,"%.10f" % fark2,"%.10f" % fark3)
    h=h/10.0
