import random
num = random.randint(1,100)
i = int(input("input a number: " ))
while i != num:
    if i > num:
       i = int(input("input smaller:"))
    elif i < num:
       i = int(input("input bigger:"))
print("congratulation!")
