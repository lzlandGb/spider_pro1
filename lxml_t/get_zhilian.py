import random
import urllib.request
import urllib.parse
import os
import re
import time


from lxml import etree


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='etree.log')
def get_page_source(url=None):
    headers = {
        "User-Agent": "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
    }
    # 避免url为空的问题
    try:
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        return response.read().decode('utf-8')
    except ValueError as e:
        logger.debug('url格式有误')


def get_page_urls():
    '''
    'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&isadv=0&sg=39e470246d7e4727944af8c5e9417893&p=4'
    'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%8c%97%e4%ba%ac&kw=python&isadv=0&sg=39e470246d7e4727944af8c5e9417893&p=4'
    'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&isadv=0&sg=39e470246d7e4727944af8c5e9417893&p=2'
    'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&isadv=0&sg=39e470246d7e4727944af8c5e9417893&p=3'
    '''

    # 获取网页代码
    page_source = get_page_source('https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&isadv=0&sg=39e470246d7e4727944af8c5e9417893&p=3')
    # 获取页数
    # pages = number // 60 +
    restr = '<em>(\d+)</em>'
    num = re.findall(restr,page_source)
    pages = int(num[0]) // 60 + 1

    logger.debug(pages)
    # 获取页码链接列表
    url_list = []
    for i in range(pages):
        url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&isadv=0&sg=39e470246d7e4727944af8c5e9417893&p=' + str(i+1)
        url_list.append(url)

    return url_list


    pass


def get_url_list(url=None):
    xpath = "//div[@class='newlist_list_content']//table[@class='newlist']//a[@style='font-weight: bold']/@href"
    headers = {"User-Agent":"Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"}
    try:
        request = urllib.request.Request(url=url, headers=headers)
        # 获取网页代码
        response = urllib.request.urlopen(request)
        # 捉取链接
        html = etree.HTML(response.read().decode('utf-8'))
        url_list = html.xpath(xpath)

        return url_list
    except ValueError as e:
        logger.debug(e)
        logger.debug('url格式有误')
        logger.debug('职位url列表获取失败')


def get_info(url = None):
    try:
        xpath = "//div[@class='tab-inner-cont']/p/text()"
        headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"}
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        print(response.status)
        # print(response.read().decode('utf-8'))
        html = etree.HTML(response.read().decode('utf-8'))
        str = ''
        list = html.xpath(xpath)
        i = 0
        # 去掉换行符
        for s in list:
            if s == '\n':
                del list[i]
            i+=1
        i = 0
        for s in list:
            if s == '\n':
                del list[i]
            i+=1
        i = 0
        for s in list:
            if s == '\n':
                del list[i]
            i+=1
        str = ''
        for s in list:
            str = str + s + '\t\n'
        # 写入文本
        # with open(os.getcwd()+'/need.txt', 'w') as f:
        #     f.write(str)
    except ValueError as e:
        logger.debug(e)
        logger.debug('url格式有误')
        logger.debug('岗位要求信息获取失败')


if __name__ == '__main__':
    page_num = 0
    page_url_list = get_page_urls()
    file = open(os.getcwd() + '/zhaopin.txt', 'a')
    start_time = 0
    for page_url in page_url_list:
        file.write("这里是第 " + str(page_num) + "页的url    " + page_url)
        logger.debug("这里是第 " + str(page_num) + "页的url    " + page_url)
        url_num = 0
        url_list = get_url_list(page_url)
        for url in url_list:
            file.write("这里是第 " + str(page_num) + "页的第" + str(url_num) + '条url    ' + url )
            logger.debug("这里是第 " + str(page_num) + "页的第" + str(url_num) + '条url    ' + url )
            s = get_info(url)
            time.sleep(random.random()+2)
            if  s == None:
                file.write("这里是第 " + str(page_num) + "页的第" + str(url_num) + '条url    ' + url + '该url没有获取到数据')
                logger.debug("这里是第 " + str(page_num) + "页的第" + str(url_num) + '条url    ' + url + '该url没有获取到数据')
            elif len(s) < 1:
                file.write("这里是第 " + str(page_num) + "页的第" + str(url_num) + '条url    ' + url + '该url没有获取到数据')
                logger.debug("这里是第 " + str(page_num) + "页的第" + str(url_num) + '条url    ' + url + '该url没有获取到数据')
            else:
                file.write(s)

            url_num+=1
        page_num += 1
    file.close()
    end_time = time.time()
    print('信息获取并写入文件耗费' + str(end_time - start_time))
    print('main over')


'''
    待解决问题： 数据捉取不完整，xpath只能获取一个目标值，无法避免突发情况
    hedgehog = 'http://jobs.zhaopin.com/CC131343479J00052176011.htm'
'''