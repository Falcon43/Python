import numpy as np
import time,sys


print("\nmemory efficiency  |  numpy  vs  list ")
print("\nlist space occupied: ")
list1 = range(1000)
print(sys.getsizeof(5)*len(list1))

print("\nnumpy space occupied: ")
numpy1 = np.arange(1000)
print(numpy1.size*numpy1.itemsize)


print("\n\nspeed  |  numpy  vs  list ")

size = 10000000

l1 = range(size)
l2 = range(size)

n1 = np.arange(size)
n2 = np.arange(size)

start = time.time()

result = [(x+y) for x,y in zip(l1,l2)]
print("\nAdded list: ")
print(result)
print("\nspeed of list during addition: ")
print((time.time()-start)*1000)

start = time.time()

result =  n1+n2
print("\nAdded numpy: ")
print(result)
print("\nSpeed of numpy during addition: ")
print((time.time()-start)*1000)