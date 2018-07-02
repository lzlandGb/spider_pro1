import urllib.request
import os
import re


from lxml import etree


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='jiaobenzhijia.log')
# 获取网页代码
def get_page_source(url = None):
    try:
        headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"}
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        return response.read().decode('gb2312')
    except ValueError as e:
        logger.error(e)
        logger.debug('参数不正确， 路由错误')


# 获取网页中需要的url
def get_info_url(url):
    page_source = get_page_source(url)
    xpath = "//div[@class='artlist clearfix']/dl/dt/a/@href"
    xpath2 = "//div[@class='artlist clearfix']/dl/dt/a/@title"
    html = etree.HTML(page_source)
    url_list = html.xpath(xpath)
    new_url_list = []
    for url in url_list:
        new_url_list.append('https://www.jb51.net' + url)

    title_list = html.xpath(xpath2)

    wanna_list = []
    if len(new_url_list) == len(title_list):
        for i, j in zip(title_list, new_url_list):
            wanna_list.append({i:j})
        return wanna_list
    else:
        return 0


# 获取每个分页的链接
def get_page_url():
    'https://www.jb51.net/list/list_6_1.htm'
    'https://www.jb51.net/list/list_6_2.htm'
    'https://www.jb51.net/list/list_6_3.htm'
    # 获取总页数
    page_source = get_page_source('https://www.jb51.net/list/list_6_3.htm') #  'https://www.jb51.net/list/list_6_3.html'
    html = etree.HTML(page_source)
    restr = '页次：3/(\d+) 每页'
    page_count = re.findall(restr, page_source)
    page_count = int(page_count[0])
    # page_c = page_count // 40
    # if page_count % 40 > 0:
    #     page_c = page_count // 40 + 1
    page_url_list = []
    for i in range(page_count):
        url = 'https://www.jb51.net/list/list_6_' + str(i+1) + '.htm'
        page_url_list.append(url)

    return page_url_list


if __name__ == '__main__':
    page_url_list = get_page_url()
    i = 0
    for url in page_url_list:
        logger.debug('这里是分割线-------------------------------------------')
        logger.debug('这里是分割线-------------------------------------------')
        logger.debug('这里是分割线-------------------------------------------')
        logger.debug('page' + str(i) + '页' + url)
        urls = get_info_url(url)
        for u in urls:
            logger.debug(u)

        i += 1