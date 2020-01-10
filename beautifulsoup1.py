#coding:utf-8
import re
import urllib.request
from bs4 import BeautifulSoup
import time

class pachong():
    url = r""
def geturl(url):
    page = urllib.request.urlopen(url)
    time.sleep(2)
    html = page.read().decode("utf-8")
    return html

def getimage(html):
    soup = BeautifulSoup(html,"lxml")
    imagelist = soup.select(r'img[class="BDE_Image"]')
    imageurls = [imageurl['src'] for imageurl in imagelist]
        
    x = 1
    for img in imageurls:
        urllib.request.urlretrieve(img,r'D:\Program Files\python\{}.jpg'.format(x))
        x+=1
"""
urls = [r'http://tieba.baidu.com/p/4444472295?pn={}'.format(str(i)) for i in range(1,33)]

for url in urls:
    html = geturl(url)
    getimage(html)
"""


