import random
def creat (num,long):
    b=[]
    string = "1234567890qwertyuiopasdfghjklzxcvbnmQERTYUIOPASDFGHJKLZXCVBNM"
    for i in range(num):
        a = ""
        for j in range(long):
            a += random.choice(string)
        b.append(a)
    for k in range(len(b)):
        print (b[k])

creat (10,10)
