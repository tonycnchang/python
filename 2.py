import numpy as np

a = np.arange(1,13).reshape((3,4))
#print(a)
#print(a[1,2])
#print(a[1,:])
#print(a[1,1:3])
'''
for row in a:
    print(row)
for column in a.T:
    print(column)
'''
print(a.flatten())
for item in a.flat:
    print(item)
