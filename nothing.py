l=['zhang','tian','hao','shuai']
def fun (a,b,c,d):
    print ("a : %s" % a)
fun(*l)



print ('#'*40)

def icecream_machine( x=3 , y="草莓" ):
    print ("制作一个",x,"元",y,"口味的冰淇凌")

first = input("请输入价格：")
second = input("请选择口味：")

icecream_machine ( first , second )

print ("#"*40)