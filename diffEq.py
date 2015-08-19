#Differential equation        2nd order
#http://sam-marsh.staff.shef.ac.uk/mas115/docs/PYTHON-Lecture10.pdf

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def deriv(y,t):
    uprime = y[1]
    wprime = - 3*y[0] + np.sin(t)
    yprime = np.array([uprime, wprime])
    return yprime


start=0
end=10
numsteps=1000
time=np.linspace(start,end,numsteps)
y0=np.array([1, 1])


y=integrate.odeint(deriv,y0,time)

plt.plot(time,y[:,0])
plt.show()


