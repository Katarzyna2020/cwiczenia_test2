import matplotlib.pyplot as plt
import numpy as np
import teoria as t

def plot_noerr(x,y):
    plt.xscale("log")
    plt.scatter(x,y)

def plot_err(x,y,err):    
    plt.xscale("log")
    plt.errorbar(x,y,yerr = err,fmt='ro',ls='none')   
    
def plot_th_tlumienie():
    ft=np.logspace(1,7,500)
    plt.xscale("log")    
    plt.plot(ft,t.tlumienie(ft,1e3,1e-9),'b')

def plot_th_phaseshift():    
    ft=np.logspace(1,7,500)
    plt.xscale("log")
    plt.plot(ft,t.phaseshift(ft,1e3,1e-9),'b')

def plot_tlumienie_after_fit(par):
    ft=np.logspace(1,7,500)
    plt.xscale("log")    
    plt.plot(ft,t.tlumienie_fit(ft,*par),'g')
    plt.xlabel(r'$\omega$')
    plt.ylabel(r'$\frac{U_{wy}}{U_{we}}$')

def plot_phaseshift_after_fit(par):
    ft=np.logspace(1,7,500)
    plt.xscale("log")    
    plt.plot(ft,t.phaseshift_fit(ft,*par),'g')

    
