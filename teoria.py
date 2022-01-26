import numpy as np
def tlumienie_fit(f,a):
    return 1./(np.sqrt((2*np.pi*a*f)**2+1))
def tlumienie(f,R,C):
    return 1./(np.sqrt((2*np.pi*R*C*f)**2+1))
def phaseshift_fit(f,a):
    return (180.*np.arctan(2*np.pi*f*a))/np.pi
def phaseshift(f,R,C):
    return (180.*np.arctan(2*np.pi*f*R*C))/np.pi
