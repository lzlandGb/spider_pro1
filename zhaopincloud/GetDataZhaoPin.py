#!/usr/local/python3/bin/python3
'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python&sm=0&p=1'
import selenium
import selenium.webdriver
import urllib.parse
import os
import re
import urllib.request


from Tools.tools import debug_log


logger = debug_log(os.getcwd())

def get_pages():
    pass

def get_url(addr = '深圳', search_word='python'):
    data = {
        'jl': addr,
        'kw': search_word
    }
    data = urllib.parse.urlencode(data)
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'+ data + '&sm=0&p=1'
    logger.debug(url)
    driver = selenium.webdriver.PhantomJS()
    driver.get(url)

    page_source = driver.page_source

    # logger.debug(page_source)
    restr = 'href=(\s\S*?)'
    src_pattern = re.compile(restr)

    url_list = src_pattern.findall(page_source)

    logger.debug(url_list)

    for url in url_list:
        print(url)


def get_data():
    driver = selenium.webdriver.PhantomJS()
    driver.get('http://jobs.zhaopin.com/187965628251101.htm?ssidkey=y&ss=201&ff=03&sg=c792df342d114f048976095ee2b5d3da&so=11')

    str = driver.find_element_by_xpath('//span[@style="font-size:16px;font-family:宋体"]')

    logger.debug(type(str))



    pass


if __name__ == '__main__':
    get_data()