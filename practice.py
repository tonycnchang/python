#1
list1=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):

            if (i!=k)and(i!=j)and(j!=k):
                num = i * 100 + j * 10 + k
                list1.append(num)
print(list1)
print(len(list1))

for x in range(len(list1)):
    print (list1[x])

