# encoding:utf-8
import  urllib.request
import os


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='check_proxy.log')

'''
httpproxy=urllib2.ProxyHandler({"http":"10.36.132.41:808"})#代理无需账号
opener=urllib2.build_opener(httpproxy)#创建一个打开器
request=urllib2.Request("http://www.baidu.com") #访问百度
response=opener.open(request)#打开网页，内置代理服务器
print response.read()
'''

# 测试代理是否可用
#  测试个多代理
def check_proxys(proxy_dict_list):
    if not isinstance(proxy_dict_list, list) and not isinstance(proxy_dict_list[0], dict):
        logger.debug("请输入正确的代理")
    i = 0
    for proxy_dict in proxy_dict_list:
        proxy=urllib.request.ProxyHandler(proxy_dict)
        # nohttpproxy=urllib.request.ProxyHandler({}) #空代理
        opener=urllib.request.build_opener(proxy)
        request=urllib.request.Request("http://www.baidu.com/") #代理访问，URL必须完整，
        try:
            response = opener.open(request, timeout=4)
            logger.debug(str(proxy_dict) + " 该代理可正常使用")
        except urllib.error.URLError as e:
            proxy_dict_list[i] =  None
            logger.debug(str(proxy_dict) + "该代理无法使用" + '请求超时')

        finally:
            i += 1

        # 筛选有用的proxy并返回
        new_proxy_dict_list = []
        for proxy in proxy_dict_list:
            if proxy == None:
                continue
            new_proxy_dict_list.append(proxy)

        return new_proxy_dict_list

# 测试单个代理
def check_proxy(proxy):
    if not isinstance(proxy, dict):
        logger.debug("非代理，无法测试")
    proxy_handler=urllib.request.ProxyHandler(proxy)
    # nohttpproxy=urllib.request.ProxyHandler({}) #空代理
    opener=urllib.request.build_opener(proxy_handler)
    request=urllib.request.Request("http://www.baidu.com/") #代理访问，URL必须完整，
    try:
        response = opener.open(request, timeout=4)
        logger.debug(str(proxy) + ' 该代理可以正常使用')
    except urllib.error.URLError as e:
        logger.debug(str(proxy) + "该代理无法使用"  + '请求超时')


if __name__ == '__main__':
    check_proxys([{'http':'3435.4.34.324.5'}])