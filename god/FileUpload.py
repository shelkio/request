# _*_ coding: utf-8 _*_
from selenium import webdriver
import win32clipboard as wincb
import win32api
import win32con

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.find_element_by_id('kw').send_keys('1234')
win32api.keybd_event(13,0,win32con.KEYEVENTF_EXTENDEDKEY,0)
win32api.keybd_event(108,0, win32con.KEYEVENTF_KEYUP, 0)
