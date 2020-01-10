from beautifulsoup2 import pachong

bizhi = pachong()


bizhi.url = [r'http://tieba.baidu.com/p/3910118183?pn={}'.format(str(i)) for i in range(1,4)]
for urls in bizhi.url:
    bizhi.url = urls
    bizhi.getimage()

