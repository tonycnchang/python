

class zhanshi():
    xingming = ""
    zhongzu = "人族"
    xingbie = "男"
    xue = 1000
    mo = 200

    def __init__(self,xingming=input("请输入姓名："),zhongzu="牛头人",xingbie="男"):
        self.xingming = xingming
        self.zhongzu = zhongzu
        self.xingbie = xingbie


MT = zhanshi()
print ("姓名："+ MT.xingming, "性别："+ MT.xingbie, "种族："+ MT.zhongzu, "血量：%s"% MT.xue, "魔量：%s"% MT.mo, sep = "\n##########\n")
