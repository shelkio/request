# _*_ coding: utf-8 _*_
import urllib

#请求百度网页
re = urllib.urlopen('http://www.baidu.com')
print (re.info())