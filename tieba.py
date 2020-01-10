
import beautifulsoup1

urls = [r'http://tieba.baidu.com/p/4444472295?pn={}'.format(str(i)) for i in range(1,33)]
for url in urls:
    html = beautifulsoup1.geturl(url)
    beautifulsoup1.getimage(html)
