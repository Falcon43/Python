import numpy as np

N = np.array([(1,2,3,4),(2,3,4,6)])

print("Dimension: %s" %N.ndim)
print("itemsize: %s" %N.itemsize)
print("dtype: %s" %N.dtype)
print("size: %s" %N.size)


print("\n\nShape  &  Reshape:")
print("shape: "+str(N.shape))
print(N)
N = N.reshape(1,8)
print("shape: "+str(N.shape))
print(N)
N = N.reshape(4,2)
print("shape: "+str(N.shape))
print(N)


print("\n\nSlicing:")
N2 = np.array([(1,2,3,4),(2,4,5,6),(7,8,9,10)])
print(N2)
print(N2[0:,3])
print(N2[0:2,3])
print(N2[2,1:3])



print("\n\nlinspace:")
lins = np.linspace(1,3,10)
print(lins)


N2 = np.array([(1,2,3,4,1),(2,4,5,6,0),(7,8,9,10,0)])
print("\n\nMin: %s" %N2.min())
print("Max: %s" %N2.max())
print("Sum: %s" %N2.sum())




print("\n\n\naxis 1  &  axis 0:")
N3 = np.array([(1,2,3),(2,3,4)])
print("Sum of axis 0 : %s" %N3.sum(axis=0))
print("Sum of axis 1 : %s" %N3.sum(axis=1))



print("\n\n\nMathematical functions:")
print("Squareroot: %s" %np.sqrt(N3))
print("Standard Deviatiom: %s" %np.std(N3))



print("\n\n\nMatrix basic operation:")
a = np.array([(1,2,3,4),(2,3,4,6)])
b = np.array([(1,2,3,4),(2,3,4,6)])
print("Add numpy: %s" %(a+b))
print("Subtraction numpy: %s" %(a-b))
print("Multiplication numpy: %s" %(a*b))
print("Division numpy: %s" %(b/a))



print("\n\n\nVertical Stacking and Horizontal Stacking:")
print("\nvstack:")
print(np.vstack((a,b)))
print("\nhstack:")
print(np.hstack((a,b)))



print("\n\n\nSingle ROW: ravel()")
print(a.ravel())





print("\n\n\nSingle ROW: ravel()")
print(a.ravel())
