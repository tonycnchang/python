import numpy as np

a = np.array([1,3,6,8])
b = np.array([2,7,3,9])

c = np.vstack((a,b))   #vertical stack  横向合并
d = np.hstack((a,b,a))   #horizontal stack  纵向合并

#print(c,"\n",d)

aa = a[:,np.newaxis]
bb = b[:,np.newaxis]
dd = np.hstack((aa,bb,bb))

ee = np.concatenate((aa,bb,aa),axis=1)   



e = np.split(c,2,axis=1)   #等分割

a1 = np.array([[1,3,6,8,6,5,2],
               [2,6,5,9,7,5,8]])

f = np.array_split(a1,3,axis=1)   #不等分割

#print(np.vsplit(c,2))     #横向分割
#print(np.hsplit(c,2))   #纵向分割


b1 = b.copy()    #不关联
b[2] = 33
#print(b1,b)


