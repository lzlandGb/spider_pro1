import requests

def get_12306_pagesource():
    res = requests.get(url = 'https://www.12306.cn', verify=False)
    print(res.content.decode('utf-8'))

# 使用urllib.rquest访问
def get_12306_pagesource2():
    import urllib.request
    import ssl
    context = ssl._create_unverified_context()
    resp = urllib.request.urlopen(url = 'https://www.12306.cn', context= context)
    print(resp.read().decode('utf-8'))

if __name__ == '__main__':
    # get_12306_pagesource()
    get_12306_pagesource2()