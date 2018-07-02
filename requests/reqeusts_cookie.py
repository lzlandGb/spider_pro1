import requests

def get_baidu_cookie():
    cookies = {"BDORZ":"10086"}
    res = requests.get("http://httpbin.org/cookies", cookies=cookies)
    print(res.cookies)
    print(res.text)


# 使用urllb.request获取访问百度的cookie
def get_baidu_cookie2():
    import urllib.request
    import http.cookiejar
    res = urllib.request.urlopen("http://www.baidu.com")

    # 获取访问百度时的cookie
    cookies = http.cookiejar.CookieJar()
    cookie_process = urllib.request.HTTPCookieProcessor(cookies)
    opener = urllib.request.build_opener(cookie_process)

    response = opener.open('http://www.baidu.com')
    for i in dir(cookies):
        print(i)

if __name__ == '__main__':
    get_baidu_cookie()