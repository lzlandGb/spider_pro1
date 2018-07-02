import requests

def get_baidu_pagesource():
    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=ps4&rsv_pq=8fc5d0490002ff96&rsv_t=e84bfFEsGgyc7gluGaTWI0lbHOErGFx9h3kJBoPVXdeBh3dgKBJRIwIJEYc&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&inputT=1013&rsv_sug4=2020'
    data = {
        'wd':'ps4'
    }

    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }
    response = requests.get('http://www.baidu.com/s?', params=data, headers=headers)
    print(response.encoding)
    print(response.content.decode('utf-8'))
    print(response.url)

# 使用urllib.request
def get_baidu_pagesource2():
    import urllib.request
    import urllib.parse
    url = "http://www.baidu.com/s?"
    data = {
        'wd': 'ps4'
    }
    data = urllib.parse.urlencode(data)
    url = url + data
    request = urllib.request.Request(url=url)
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))
    print(response.url)

if __name__ == '__main__':
    # get_baidu_pagesource()
    get_baidu_pagesource2()