import numpy as np

# need  sum s+b as scalar
W = np.random.randn(4, 4, 3)
b = np.random.randn(1, 1, 1)
s = np.sum(W)   # np.sum() gives integer
print(s)
print(b)        # b is still array
print(s+b)      #will result in an 3D array output of this sum
print(float(s+b))   # need to use float to cast array to scalar
print( s + float(b) , "\n")  #will not result in an 3D array output of this sum, but a scalar output


# need  sum s+b as scalar when b is obtained from new_b
new_b = np.random.randn(1, 1, 1, 10)
print(new_b)
b = new_b[:,:,:,1]    # on slicing b , it's still a 3D array
print(b)
print(s+b)    #will result in an 3D array output of this sum
print( s + float(b) )  #will not result in an 3D array output of this sum, but a scalar output

"""
Output:

3.4050427852171303
[[[0.46932232]]]
[[[3.8743651]]]
3.874365100386826
3.874365100386826 

[[[[ 1.18973494 -1.39765882  0.09553642  0.61802283 -2.2521763
     2.12645673  0.49754439 -0.96717106  0.91325472 -1.10083306]]]]
[[[-1.39765882]]]
[[[2.00738396]]]
2.0073839643048403

"""