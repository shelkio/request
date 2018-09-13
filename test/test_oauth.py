# _*_ coding: utf-8 _*_
import requests
from requests.auth import AuthBase

Base_Url = 'https://api.github.com'


def build_url(end_point):
    return '/'.join([Base_Url,end_point])

def oauth_auth():
    headers = {'Authorization': 'token 886327994336cc6a1de3113831596e2063cb266c'}
    # 获取user/email信息
    response = requests.get(build_url('user/emails'),headers=headers)
    print (response.status_code)
    print (response.elapsed)
    print (response.text)
    print (response.request.headers)

class GithubAurh(AuthBase):
    def __init__(self,token):
        self.token=token

    def __call__(self, r):
        # 给request 添加headers
        r.headers['Authorization'] = '  '.join(['token',self.token])
        return r

def oauth_request_advance():
        auth = GithubAurh('886327994336cc6a1de3113831596e2063cb266c')
        response = requests.get(build_url('user/emails'),auth=auth)
        print (response.text)

oauth_request_advance()
