#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: image-down.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-06-30
#Description: 

"""一个实现煎蛋无聊图的下载,给自己的生活添点乐子"""
import urllib
import urllib2
import time
from bs4 import BeautifulSoup
f = urllib2.urlopen(
       # url = "http://jandan.net/pic"
       url = "http://jandan.net/pic/page-4924#comments"
        )
html = f.read()
#上边的是读取网页
soup = BeautifulSoup(html)
#这个部分是将读取到的html传给BeautifulSoup,返回一个soup对象
image = soup.find_all("img")
print type(image)

""" 在这个soup对象中找img这个标签，
    打印这个标签，能看到无数地址
    发现这些地址中有些是有些是gif图,有些是jpg，他们有区别所以分开
    所有的地址都放在了list中,
"""
gif = []
for c,i in enumerate(image):#这个 enumerate可以返回每个元素和元素的序号，可以查查
    if "org_src" in str(i):
        gif.append(i)#是gif的图放到gif这个list中
        del image[c]#将对应的放到gif中的那个元素从image中删除
    
print image
print gif
image_end = []
for a in image:
    image_end.append(str(a)[10:-3])#这句是将图片的url处理一下

print image_end

gif_end = []
for b in gif:
    gif_end.append(str(b)[14:79])

print gif_end
name = 0
path = "image/"
for gif_i in gif_end:
  #  gif_write = open(str(gif_i)[50:],"w")
 #   gif_file = urllib.urlopen(str(gif_i)[50:]).read()
 #   gif_write.write(gif_file)
 #   time.sleep(3)
    name = name+1
    urllib.urlretrieve(str(gif_i),path+str(name)+".gif")
    print "a"
print "end"
        

