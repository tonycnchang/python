import numpy as np

array1 = np.array([[12,11,13],[2,3,4]])
array2 = np.array([[3,4,5],[21,24,25],[12,14,11]])
array3 = np.array([1,2,3],[5,6,7])

'''
print (array1,array2,array3,sep='\n*******\n')

print(array1.ndim)
print(array2.ndim)
print(array2.ndim)

print(array1.shape)
print(array2.shape)
print(array3.shape)
'''
aaa = np.dot(array1,array2)
bbb = array1.dot(array2)

ccc = np.random.random((3,4))
d = np.sum(ccc,axis=0)   #axis=0对列进行计算，axis=1对行进行计算

e = np.arange(0,15).reshape((3,5))

#print(np.mean(e))
#print(e.mean())
#print(np.average(e))
#print(np.median(e))    #中位数
#print(np.cumsum(e))#累加
#print(np.diff(e)) #后减前
#print (np.nonzero(e))  #非零
#print(np.sort(array2))  #顺序排列
#print(np.transpose(e)) #行列转换
#print(e.T)   #行列转换
#print(np.clip(e,5,9))  #小于5的数变成5，大于9的数，变成9

#c=array1-array3
#c=array1+array3
#c=array1*array3
#c=array1/array3
#c=array1**2
#print(c)       #计算

#f = np.sin(array1) #np.cos(), np.tan(), np.ctan()
#print (f)   #三角函数计算

#print(array1<8)  #">","=="等输出False或True
