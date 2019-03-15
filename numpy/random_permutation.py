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