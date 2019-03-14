import numpy as np

W = np.random.randn(4, 4, 3)
b = np.random.randn(1, 1, 1)
s = np.sum(W)
print(s)
print(b)
print(s+b)
print(float(s+b))
print( s + float(b) )