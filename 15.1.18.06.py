import numpy as np 


b = np.array([[1,0,0],[0,1,0], [0,0,1], [0,0,0]])
t1 = np.array([2,2,3])
t2 = np.array([1,1,1])
print(np.dot(t1,np.transpose(t2)))
bt = np.transpose(b)
P =np.dot(np.dot(b, np.linalg.inv(np.dot(bt,b))), bt)
print(P) 
