# _*_ coding: utf-8 _*_
import re

str = "欢迎使用版权家平台,验证码为8493。版权家-版权服务专家。欢迎使用版权家平台,验证码是9407。版权家-版权服务专家。username=111"
B=unicode(str, 'UTF-8')
C=re.findall(u"验证码.(\w*)",B)#
print C[0]
#输出['23']