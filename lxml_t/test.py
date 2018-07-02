import urllib.request
import urllib.parse
import os
import re


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
    except Exception as e:
        logger.debug(e)
        logger.debug('网页代码获取失败')


def get_page_urls():
    '''
    'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&isadv=0&sg=39e470246d7e4727944af8c5e9417893&p=4'
    'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%8c%97%e4%ba%ac&kw=python&isadv=0&sg=39e470246d7e4727944af8c5e9417893&p=4'
    'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&isadv=0&sg=39e470246d7e4727944af8c5e9417893&p=2'
    'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&isadv=0&sg=39e470246d7e4727944af8c5e9417893&p=3'
    '''
    try:

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
    except Exception as e:
        logger.debug(e)
        logger.debug('页码链接获取失败')


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
    except Exception as e:
        logger.debug('职位url列表获取失败')






def get_info(url = None):
    try:
        xpath = "//div[@class='tab-inner-cont']/p/text()"
        headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"}
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
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
        print(str)
    except ValueError as e:
        logger.debug(e)
        logger.debug('url格式有误')
        logger.debug('岗位要求信息获取失败')
    except Exception as e:
        logger.debug('岗位要求信息获取失败')


if __name__ == '__main__':
    page_url_list = get_page_urls()
    for page_url in page_url_list:
        url_list = get_url_list(page_url)
        for url in url_list:
            get_info(url)




'''
    待解决问题： 数据捉取不完整，xpath只能获取一个目标值，无法避免突发情况
    hedgehog = 'http://jobs.zhaopin.com/CC131343479J00052176011.htm'
'''