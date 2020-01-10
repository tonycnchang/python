import numpy as np

a = np.array([[1,0,0],[0,1,0],[0,0,1]])
b = np.array([[0,-1,0],[1,0,0],[0,0,1]])

c= np.dot(a,b)
d= a*b
print(c)
print(d)
