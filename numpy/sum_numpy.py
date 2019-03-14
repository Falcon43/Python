import numpy as np

W = np.random.randn(4, 4, 3)
b = np.random.randn(1, 1, 1)
s = np.sum(W)   # np.sum() gives integer
print(s)
print(b)        # b is still array
print(s+b)
print(float(s+b))   # need to use float to cast array to scalar
print( s + float(b) )

"""
Output:

1.3139701919235667
[[[0.29986574]]]
[[[1.61383594]]]
1.6138359360636723
1.6138359360636723

"""