#coding:utf-8
import re
import urllib.request

def gethtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode("UTF-8")
    return html

def getimage(html):
    regule = r'src="(.+?\.jpg)" size'
    imagere = re.compile(regule)
    imagelist = re.findall(imagere,html)
    print (imagelist)

"""
    x = 30
    for imageurl in imagelist:
        urllib.request.urlretrieve(imageurl,'%s.jpg' % x)
        x+=1
"""

html = gethtml("http://tieba.baidu.com/p/1300684557")
getimage(html)

