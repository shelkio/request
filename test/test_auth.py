# _*_ coding: utf-8 _*_
import requests

Base_Url = 'https://api.github.com'


def build_url(end_point):
    return '/'.join([Base_Url, end_point])


def basic_auth():
    response = requests.get(build_url('user'), auth=('goodaaa', 'li981230'))
    print (response.status_code)
    print (response.text)
    print (response.request.headers)


basic_auth()
