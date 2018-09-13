# _*_ coding: utf-8 _*_
import requests
import json

session_id='80oqunfr885n7o8bhlpto0r247'
#调用接口
response = requests.get('http://ggtest.bqj.cn/ggtest/GgContribute/getTagList.json?session_id='+session_id)
response1=json.dumps(response.json(),ensure_ascii=False,indent=3)
print (response1)
