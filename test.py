import numpy as np 


A = np.array([[1,-1], [1,1], [1,2]])
b = np.transpose(np.array([7,7,21]))

At = np.transpose(A)

AAtinv = np.linalg.inv(np.dot(At, A))

x = np.dot(np.dot(At, b), AAtinv)

print(x)
