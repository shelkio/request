# _*_ coding: utf-8 _*_
import win32clipboard as wincb
import win32api
import win32con
class Analog:
    #复制链接
    def CopyUrl(self,url):
        wincb.OpenClipboard()
        wincb.EmptyClipboard()
        wincb.SetClipboardData(win32con.CF_TEXT,url)

    @staticmethod
    #模拟键盘ctrl+v 复制
    def Paste():
        win32api.keybd_event(17,0,0,0) #ctrl键位码是17
        win32api.keybd_event(86,0,0,0) #v键位码是86
        win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

    @staticmethod
    #模拟键盘enter 回车
    def Enter():
        win32api.keybd_event(13,0,win32con.KEYEVENTF_EXTENDEDKEY,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)






