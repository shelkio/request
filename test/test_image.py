# _*_ coding: utf-8 _*_
import requests
import os
import time
from contextlib import closing
def download_image():

    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1504068152047&di=8b53bf6b8e5deb64c8ac726e260091aa&imgtype=0&src=http%3A%2F%2Fpic.baike.soso.com%2Fp%2F20140415%2Fbki-20140415104220-671149140.jpg'

    response = requests.get(url, stream = True)

    file_path = os.path.dirname(os.getcwd()) + '/image/'
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_name = file_path + rq + '.png'
    with closing(requests.get(url,stream = True)) as response:
        # 打开一个空的png文件，相当于创建一个空的txt文件，wb表示写文件
        with open(screen_name,'wb') as file:
            # 每128个流遍历一次
            for date in response.iter_content(128):
                # 把流写入到文件，这个文件最后写入完成的就是 selenium.png
                file.write(date) # date相当于一块一块数据写入到我们的图片文件中

    print (response.status_code)


if __name__ == '__main__':
    download_image()