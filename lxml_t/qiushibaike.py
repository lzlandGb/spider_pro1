import urllib.request
import requests
import os


from lxml import etree
from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='qiushi.log')

def get_qiushi():
    # 获取网页代码
    url = 'https://www.qiushibaike.com/8hr/page/2/'
    headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"}
    request = urllib.request.Request(url= url, headers=headers)
    response = urllib.request.urlopen(request)
    print(response.geturl())
    # 数据解析
    page_source = response.read().decode('utf-8')
    html = etree.HTML(page_source)
    xpath =  "//div[@class='col1']//div[@class='content']/span/text()"
    str_list = html.xpath(xpath)
    str = ''
    for s in str_list:
        s = s.strip()
        str += s + '\t\n\n\n'
    logger.debug(str)
    # 返回获取数据列表


if __name__ == '__main__':
    get_qiushi()