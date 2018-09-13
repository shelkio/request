# _*_ coding: utf-8 _*_
import json
import requests
from requests import exceptions


URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_ouput(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def custom_request():
    from requests import Request, Session
    s = Session() #初始化一个session
    headers = {'User-Agent':'fake1.3.4'}# fake是伪装的意思，就是设置一个陷阱
    request = Request('GET',build_uri('user/emails'),auth=('goodaaa','li981230'),headers=headers)
    prepped = request.prepare() #初始化一个prepare对象，用来包装请求的headers和body
    print (prepped.body) #打印出来现在为空，因为目前还没有发送请求
    print (prepped.headers)

    response = s.send(prepped, timeout=5) #通过session对象调用发送请求，内容是prepped包装好的请求
    print (response.status_code)
    print (response.headers)
    print (response.text)


if __name__ == '__main__':
    custom_request()
