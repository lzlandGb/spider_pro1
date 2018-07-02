import urllib.parse
import urllib.request
import os
import json
import ssl


from Tools.tools import debug_log
logger = debug_log(os.getcwd(),name='debug.log')
# 使用伪装浏览器以及标准url规范爬取智联招聘
def get_zhilian(addr='深圳', position='python'):
    "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python&sm=0&p=1"
    addr = {'jl': addr}
    addr = urllib.parse.urlencode(addr)
    position = {'kw': position}
    position = urllib.parse.urlencode(position)
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?' + addr + '&' + position + '&sm=0&p=1'

    headers = {
        'User-Agent': "User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"
    }

    request = urllib.request.Request(url = url, headers = headers)


    response = urllib.request.urlopen(request)

    print(response.read().decode())

    return response



def get_51job(addr = '深圳',position = 'python'):
    "https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    if addr == '四川':
        url = "https://search.51job.com/list/090000,000000,0000,00,9,99," + position + ",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    elif addr == '北京':
        url = "https://search.51job.com/list/010000,000000,0000,00,9,99," + position + ",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

    else:
        url = "https://search.51job.com/list/040000,000000,0000,00,9,99," + position + ",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

    headers = {
        'User-Agent': "User-Agent:Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"
    }

    request = urllib.request.Request(url = url, headers = headers)

    response = urllib.request.urlopen(request)


    print(response.read().decode('utf-8'))
    return response.info()



# post获取拉钩的信息
pass




# 获取豆瓣电影的信息
def get_douban_movie():
    url = "https://movie.douban.com/"
    "https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%86%B7%E9%97%A8%E4%BD%B3%E7%89%87&page_limit=50&page_start=0"
    url2 = 'https://movie.douban.com/j/search_subjects?'
    data = {
        'type': 'tv',
        'tag' : '国产剧',
        'page_limit': 50,
        'page_start': 0
    }
    data = urllib.parse.urlencode(data)
    url2 = url2 + data
    try:
        response = urllib.request.urlopen(url=url2)
    except Exception as e :
        print(e)
        return '网页请求错误'


    return response.read()


# 使用代理访问

def use_proxyhander():
    proxyhander = urllib.request.ProxyHandler({'http':'122.114.31.177'})

    opener = urllib.request.build_opener(proxyhander)

    request = urllib.request.Request('https://www.wandouip.com/?wd=ip%20%E4%BB%A3%E7%90%86&e_matchtype=2&b_scene_zt=1')

    response = opener.open(request)

    logger.debug(response.code)
    logger.debug(response.read().decode())
    return response


# 下载文件
def dow_img():
    img = urllib.request.urlretrieve('http://pic27.nipic.com/20130306/9238737_105422851000_2.jpg',filename='hello_urllib_urlretrieve.jpg')
    logger.debug(os.getcwd())
    pass



# 网页重定向
class Redirect_302(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        res = urllib.request.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        res.status = code
        res.newurl = res.geturl()

        return res
def hander_302():
    proxyhander = urllib.request.ProxyHandler({'https': '123.57.207.2'})
    opener = urllib.request.build_opener(Redirect_302,proxyhander)
    context = ssl._create_unverified_context()

    # 强调： openerDirect同urllib.request一样无法处理https请求

    res = opener.open('http://www.baidu.cn')
    logger.debug(res.read().decode())
    # logger.debug(res.newurl)
    logger.debug(res.geturl())
    logger.debug(res.status)
    logger.debug(type(opener))

    # handlers？
    # logger.debug(Redirect_302)
    # logger.debug(proxyhander)
    # return(res)


# 使用ssl函数忽略ssl证书安全
def ssl_https():
    context = ssl._create_unverified_context()
    url = 'https://www.baidu.com'
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
    }
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request,context=context)


    print(response.read().decode('utf-8'))



# urllib.request.build_oepner()实现http debug模式
def http_debug():
    http_hander = urllib.request.HTTPHandler(debuglevel=1)
    https_hander = urllib.request.HTTPSHandler(debuglevel=1)
    proxy_hander = urllib.request.ProxyHandler({'http': '123.57.207.2'})
    context = ssl._create_unverified_context()

    opener = urllib.request.build_opener(http_hander, https_hander, proxy_hander)
    # 配置到urllib.request模块
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen('https://www.baidu.com', context=context)

    logger.debug(response.read())
    logger.debug(response.info())

    return response

if __name__ == '__main__':
    http_debug()