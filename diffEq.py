#Differential equation


import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def deriv(y,t):
    yprime = np.array([3.5*y[0]])
    return yprime

start=0
end=1
numsteps=1000
time=np.linspace(start,end,numsteps)
y0=np.array([10])

y=integrate.odeint(deriv,y0,time)
plt.plot(time,y[:])
plt.show()

