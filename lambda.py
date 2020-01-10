l = (1,2,3)
g = lambda x,y,z : {"x : %s" % x,"y : %s" % y,"z : %s" % z}
print(g(*l))
print (6-3)

x = int(input(":"))
y = int(input(";"))
operate = input(":")
result = {
    "+":x + y,
    "-":x - y,
    "*":x * y,
    "/":x / y
    }
print (result.get(operate))
