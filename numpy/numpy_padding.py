import numpy as np

pad = 3
X = [[1, 2], [3, 4]]
print(np.pad(X, ((0, 0), (pad, pad)), 'constant', constant_values=(pad, pad))  , "\n")
print(np.pad(X, ((1, 0), (pad, pad)), 'constant', constant_values=(pad, pad))  , "\n")
print(np.pad(X, ((1, 0), (2, 1)), 'constant', constant_values=(pad, pad))  , "\n")
print(np.pad(X, ((1, 0), (2, 1)), 'constant', constant_values=(7, pad))  , "\n")
print(np.pad(X, ((1, 0), (2, 1)), 'constant', constant_values=(7, 8))  , "\n")
print(np.pad(X, ((1, 0), (9, 8)), 'constant', constant_values=(pad, 4))  , "\n")
print(np.pad(X, ((1, 1), (1, 1)), 'constant', constant_values=(0, 0))  , "\n")


#X = np.zeros((4,4,3,2))
X = np.random.randn(2,2,3,2)
print(X)
print(np.pad(X, ((0, 0), (1, 1), (1, 1), (0, 0)), 'constant', constant_values=(0, 0))  , "\n")