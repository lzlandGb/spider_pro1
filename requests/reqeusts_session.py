import requests
import os


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='requests_session.log')

# reqiests.session进行登陆
def login_withsession():
    session = requests.session()
    params = {
        'emp_no':	'admin',
        'password':	'admin',
    }
    login_url = 'http://demo.smeoa.com/index.php?m=&c=public&a=check_login'
    response = session.post(login_url, params)

    responsenex = session.get('http://demo.smeoa.com/index.php?m=&c=index&a=index')

    # 获取服务器响应的cookies
    cookies = response.cookies.get()
    cookies2 = response.cookies.get()

    print(responsenex.text)


# 使用requests.post登陆
def login_oswith_request_post():
    data = {
        'emp_no': 'admin',
        'password': 'admin',
    }
    login_url = 'http://demo.smeoa.com/index.php?m=&c=public&a=check_login'
    response = requests.post(url = login_url, data=data)
    print(response.text)


# 使用urllib.request的post进行登陆,  失败
def login_with_urllib_request():
    import urllib.request
    import urllib.parse
    data = {
        'emp_no': 'admin',
        'password': 'admin',
    }
    data = bytes(urllib.parse.urlencode(data), encoding='utf-8')
    login_url = 'http://demo.smeoa.com/index.php?m=&c=public&a=check_login'

    request = urllib.request.Request(url=login_url, data=data)
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))


# 使用urllib.request 配合http.cookiejar进行登陆,完成
def login_with_urllib_request_cookies():
    # 创建opener对象
    import urllib.request
    import http.cookiejar
    import urllib.parse
    cookies = http.cookiejar.CookieJar()
    cookie_process = urllib.request.HTTPCookieProcessor(cookies)

    opener = urllib.request.build_opener(cookie_process)

    # 登陆
    data = {
        'emp_no': 'admin',
        'password': 'admin',
    }
    data = bytes(urllib.parse.urlencode(data), encoding='utf-8')
    login_url = 'http://demo.smeoa.com/index.php?m=&c=public&a=check_login'
    response = opener.open(login_url, data=data)

    person_index_url = 'http://demo.smeoa.com/index.php?m=&c=index&a=index'
    responsenex = opener.open(person_index_url)

    print(responsenex.read().decode('utf-8'))



if __name__ == '__main__':
    login_withsession()
