import numpy as np

def wczytaj(nazwa):
    dane = np.loadtxt(nazwa)
    return dane 

def ilepom(dane):
    f=dane[:,0]
    return len(f)
