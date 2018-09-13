# _*_ coding: utf-8 _*_

from selenium import webdriver
#from god.GetSms import getsms
import time
from god.AnalogKeyboard import Analog

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://gg.bqj.cn/login/byPhonePwd")
driver.find_element_by_class_name('login-f-i-uname').send_keys(u'友')
driver.find_element_by_class_name('login-f-i-pwd').send_keys('333333')
#driver.find_element_by_class_name('login-f-i-pwd').send_keys(getsms.getcode())
driver.find_element_by_class_name('login-btn').click()
time.sleep(1)
driver.get('http://gg.bqj.cn/selection/myhome/addActivity')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[9]/div[2]/div[1]/div').click()
analog=Analog()
analog.CopyUrl(r'C:\Users\lishuhang\Desktop\timg2.jpg')
time.sleep(1)
analog.Paste()
analog.Enter()