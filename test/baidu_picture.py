# _*_ coding: utf-8 _*_

# coding=utf-8
"""根据搜索词下载百度图片"""
import re
import sys
import urllib
import threading
import uuid
import time
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor

reload(sys)

sys.setdefaultencoding('utf8')
lock = threading.Lock()
def getPage(keyword, page):
    page = page
    keyword = urllib.quote(keyword, safe='/')
    url_begin = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    url = url_begin + keyword + "&pn=" + str(page) + "&gsm=" + str(hex(page)) + "&ct=&ic=0&lm=-1&width=0&height=0"
    return url


def get_onepage_urls(onepageurl):
    try:
        html = requests.get(onepageurl).text
    except Exception as e:
        print(e)
        pic_urls = []
        return pic_urls
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    print pic_urls
    return pic_urls

def down_pic(pic_url,index):
    """给出图片链接列表, 下载所有图片"""
    try:
        pic = requests.get(pic_url)
        string = 'C:\\Users\\lishuhang\\Desktop\\png\\' + str(uuid.uuid1()) + '.jpg'
        f2 = open('1.txt', 'a')
        f2.write(pic_url + ' \r')
        with open(string, 'wb') as f:
            print '线程：' + threading.current_thread().name
            f.write(pic.content)
            print('成功下载第%s张图片: %s' % (str(index + 1), str(pic_url)))
            print('下载时间:%s' % time.ctime())
            index=index
    except Exception as e:
        print('下载第%s张图片时失败: %s' % (str(index + 1), str(pic_url)))
        print(e)


def downloadImgList(imgList):
    index = 0
    for imgUrl in imgList:
        with ThreadPoolExecutor(max_workers=8) as executor:
            executor.submit(down_pic, imgUrl,index)
            index+=1





    # index = 0
    # # print ('poolSupport='+str(poolSupport))
    # #print ('多线程模式')
    # # ------ 多线程编程 ------
    # threads = []
    # for imgUrl in imgList:
    #     # if printLogEnabled : print ('准备下载第'+str(index+1)+'张图片')
    #     threads.append(threading.Thread(target=down_pic,args=(imgUrl,index)))
    #     index += 1
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    # t.join() #父线程，等待所有线程结束

if __name__ == '__main__':
    keyword = '狗'  # 关键词, 改为你想输入的词即可, 相当于在百度图片里搜索一样
    page_begin = 0
    while page_begin<120:
        print 'ggggg' + str(page_begin)
        url = getPage(keyword, page_begin)
        onepage_urls = get_onepage_urls(url)
        page_begin += 60
        downloadImgList(list(onepage_urls))



    # for i in onepage_urls:
    #     all_pic_urls.append(i)
    # print all_pic_urls
    # lock = Lock()
    # pool = Pool(3,initializer=init,initargs=(lock,))
    # pool.map(down_pic, all_pic_urls)
    # pool.close()
    # pool.join()
