# 下载图片的爬虫测试

import time
import random
import os
import requests
from bs4 import BeautifulSoup as bs


def get_page_list(url):
    res = requests.get(url)
    html = res.content                # 此时结果乱码
    result = bs(html, 'html.parser')   # 此时可获得utf8

    for item in result.select('.ui-module .mala-text'):
        title = item.select('.mtitle a')[0].text
        # title = item.select('.mtitle a')[0].string    # BeautifulSoup的方法
        img_src = item.select('div a img')[0].get('src')
        data = {
            'web_url': url,
            'img_src': img_src,
            'title': title
        }
        save_img(img_src)

        print(title, img_src, end='\n\n',)


def save_img(url):  # 保存图片

    # 获取图片内容
    content = requests.get(url).content
    # 截取文件名
    filename = url.split('/')[-1]
    # 保存地址
    path = './imgs/' + filename
    print(path)

    # 判断路径是否存在
    # is_exists = os.path.exists(path)
    # print(is_exists)

    with open(path, 'wb') as f:
        f.write(content)
        print('文件保存成功！')
        f.close()


def main():
    if not os.path.exists("./imgs"):
        print("不存在")
        os.makedirs("./imgs")
    else:
        for i in range(11, 101):
            start_time = time.time()
            random_time = random.randint(1, 5)/10
            target_url = 'http://www.qiubaichengnian.com/index_%d.html' % i
            time.sleep(random_time)
            get_page_list(target_url)

            print('第%d个页面，url:%s,耗时：%d' %
                  (i, target_url, float(time.time()) - start_time), end="\n")


if __name__ == '__main__':

    main()
