import http.cookiejar
import urllib.request
import os
import re
import urllib.parse
import random


# 使用xpath获取数据不成功
# from lxml import etree


from Tools.check_proxy import check_proxy
from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='login_csdnwithcookie.log')


def login_csdnwithcookie():
    # 验证并使用代理
    '''
    HTTP
    浙江省温州市 电信
    117.87.178.31
    HTTP
    江苏省徐州市 电信
    115.223.234.116
    HTTP
    浙江省温州市 电信
    101.71.226.188

    '''
    if_proxy = False   # 是否开启代理
    if if_proxy:
        proxy = {'http':"180.118.134.107"}
        if check_proxy(proxy) == None:
            logger.debug('该代理无法使用，程序无法执行')
            return None

    login_url = 'https://passport.csdn.net/account/login'
    # 添加cookie容器
    cookie = http.cookiejar.CookieJar()
    cookie_process = urllib.request.HTTPCookieProcessor(cookie)
    if if_proxy:
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(cookie_process,proxy_handler)
    else:
        opener = urllib.request.build_opener(cookie_process)

    # 添加请求头， 冒充浏览器
    header_list = [
        [("User-Agen",
          "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50")],
        [("User-Agen",
          "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50")],
        [("User-Agen", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0")],
        [("User-Agen", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0")],
        [("User-Agen", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0")],
        [("User-Agen", " Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1")],
        [("User-Agen", " Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")],
        [("User-Agen", "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")],
        [("User-Agen", "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11")],
        [("User-Agen", "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11")],
        [("User-Agen",
          " Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")],
        [("User-Agen", " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0")],
        [("User-Agen", " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0")],
        [("User-Agen", " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1")],
        [("User-Agen", " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World")],
        [("User-Agen",
          " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0")],
        [("User-Agen", " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE")],
        [("User-Agen", " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser")],
        [("User-Agen", " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1")]
    ]
    try:
        headers = random.choice(header_list)
        opener.addheaders = headers
    except:
        logger.debug("请求头没有设置成功")
    # 获取post信息
    '''
    gps	
    username	3237651099@qq.com
    password	l2l8tc..
    rememberMe	true
    lt	LT-3774829-ThafuT3il1hROFQUKVBnvEegtglagr
    execution	e6s1
    fkid	WHJMrwNw1k/F/Zf3AruXHYA01HgjsZvZowqjqJZo5XYXrLOCIpqc3NnD24m7O300w2IHBnCroHfQbnGeGruLNyETUdaR+P3YnRPTRTiCBTkn9QBBLCeAGbZSD3EmPbcN1b2GXgZ5AQVKOJBnQglHSb8g/kaZ1QgqkTyhDb1Jcq4RkhoMiJ81hYymo5aGrFjMNY0xewvBoCqdiNVCcw5ywKPJLhdYSaxAI4fTT0FYATNl3xOP8p2kXqBjSa0uqR/otPiQZ4ehYNmk=1487582755342
    _eventId	submit
    
    data = {
        'gps':"",
        'username':"3237651099@qq.com",
        'password':"l2l8tc..",
        'rememberMe':"true",
        'lt':"",
        'execution':"",
        'fkid':"",
        '_eventId':"submit",
    }
    '''
    response = opener.open(login_url)
    page_source = response.read().decode('utf-8')
    print(page_source)
    lt_restr = 'name="lt" value="(.*)" />'
    execution_restr = 'name="execution" value="(.*?)" />'
    _eventId_restr = 'name="_eventId" value="(.*?)" />'

    lt = re.findall(lt_restr, page_source)[0]
    execution = re.findall(execution_restr, page_source)[0]
    _eventId = re.findall(_eventId_restr, page_source)[0]

    data = {
        'gps': "",
        'username': "3237651099@qq.com",
        'password': "l2l8tc..",
        'rememberMe': "true",
        'lt': lt,
        'execution': execution,
        # 'fkid': "",
        '_eventId': _eventId,
    }
    data = bytes(urllib.parse.urlencode(data), encoding='utf-8')
    # login
    response = opener.open(login_url, data = data)

    # person_page
    person_page_url = 'https://my.csdn.net/'
    responsenex = opener.open(person_page_url)

    print(responsenex.read().decode('utf-8'))
    pass


if __name__ == '__main__':
    login_csdnwithcookie()