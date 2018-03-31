import numpy as np
import matplotlib.pyplot as plt

def func1(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)  # 2: 2plots   1: horizontally 1 plot     1:   this is gng to be the 1st plot
plt.plot(t1,func1(t1),'bo', t2,func1(t2))


plt.subplot(212)  # 2: 2plots    1: horizontally 1 plot     2:  this is gng to be the 2nd plot
plt.plot(t2, np.cos(2*np.pi*t2))


plt.show()