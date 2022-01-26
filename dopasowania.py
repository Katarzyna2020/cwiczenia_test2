import numpy as np
import matplotlib.pyplot as pt
import teoria as t
from scipy.optimize import curve_fit

def dopasuj(x,y,err,fun):
    pocz=(1.e-6)
    start=np.array(pocz)
    par, cov = curve_fit(fun, x, y,p0=start,sigma=err,absolute_sigma=True)    
    print("parametry= ", par)
    print("errors= ", np.sqrt(np.diag(cov)))
    suma=0.
    for i in range(len(y)):
        suma+=(y[i]-fun(x[i],*par))**2/err[i]**2
        
    print("chi**2/liczba_stopni_swobody= ", suma/(len(y)-1))
    
    return par
