import numpy as np

#Synchronous shuffling

X = np.random.randint(0,10,size=(3,5))  # 3 row , 5 column
print("X: " ,X)
Y = np.random.randint(0,10,size=(1,5))  # 1 row , 5 column
print("Y: " ,Y)

p = np.random.permutation(X.shape[1])
print("\npermutation" , p ,"\n")

shuffled_X = X[:,p]
shuffled_Y = Y[:,p]
print("Shuffled X: " ,shuffled_X)
print("Shuffled Y: " ,shuffled_Y)


"""
Output:

X:  [[6 8 7 5 4]
 [8 4 5 7 4]
 [8 4 6 3 7]]
Y:  [[8 5 3 5 3]]

permutation [0 3 4 2 1] 

Shuffled X:  [[6 5 4 7 8]
 [8 7 4 5 4]
 [8 3 7 6 4]]
Shuffled Y:  [[8 5 3 3 5]]

"""