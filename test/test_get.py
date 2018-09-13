# _*_ coding: utf-8 _*_
import requests
import json
from requests import exceptions
URL = 'https://api.github.com'



def build_url(endpoint):
    return '/'.join([URL, endpoint])  #主要作用是拼接接口请求地址


def better_output(json_str):
    return json.dumps(json.loads(json_str), indent=4)    #采用json里面提供的方法打印出来，格式更好看


def request1_method():
    response = requests.get(build_url('session_id=1gf2sar2a09bdbo4c55oetboj2'))  #调用get方法
    print (better_output(response.text)).decode("unicode-escape")


def params_method():
    response = requests.get(build_url('session_id=1gf2sar2a09bdbo4c55oetboj2'))


def json_method():
    respons = requests.patch(build_url('user'),auth=('goodaaa','li981230'),json={'name':'333'})
    print (better_output(respons.text))
    print (respons.headers)
    print (respons.url)

def request_method():
    respons = requests.post(build_url('user/emails'),auth=('goodaaa','li981230'),json=['444@qq.com'])
    print (better_output(respons.text))
    print (respons.headers)
    print (respons.url)


def request_method1():
    respons = requests.delete(build_url('user/emails'),auth=('goodaaa','li981230'),json=['444@qq.com'])
    print (respons.headers)

def timeout_request():
    try:
        respons = requests.get(build_url('user/emails'),auth=('goodaaa','li981230'),timeout=10)
    except exceptions.Timeout as e:
        print (str(e))
    else:
        print (respons.text)

if __name__ == '__main__':
    timeout_request()