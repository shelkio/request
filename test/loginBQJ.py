# _*_ coding: utf-8 _*_
from selenium import webdriver
from god.GetSms import getsms
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://passport.bqj.cn/sso/login")
driver.find_element_by_xpath('/html/body/div/div/div/div/div/ul/li[2]').click()
driver.find_element_by_id('usernameInSignupDynamicVerifyCodeForm').send_keys('17710203585')
driver.find_element_by_xpath('//*[@id="signupDynamicVerifyCodeForm"]/div[2]/p[1]').click()
time.sleep(1)
driver.find_element_by_name('verifyCode').send_keys(getsms.getcode())
driver.find_element_by_xpath('//*[@id="signupDynamicVerifyCodeForm"]/input[3]').click()

