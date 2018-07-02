#!/usr/local/python3/bin/python3
import os
import urllib.request
import http.cookiejar
import urllib.parse
import gzip


import selenium.webdriver



from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='myprogram2.log')

# 使用open容器捉取网页cookie
def read_cookie():
    # 设置代理ip
    proxy_hander = urllib.request.ProxyHandler({'https': '123.57.207.2'})
    cookie = http.cookiejar.CookieJar()
    cookie_hander = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cookie_hander, proxy_hander)

    response = opener.open('http://www.baidu.com')

    cookies = ""
    for data in cookie:
        cookies = cookies + data.name + '=' + data.value + ";\r\n"

    logger.debug(cookies)
    return cookies


# 以文件方式保存cookie
def save_cookie():
    file = 'cookie.txt'
    cookiejar = http.cookiejar.LWPCookieJar(file)
    cookie_processor = urllib.request.HTTPCookieProcessor(cookiejar)

    opener = urllib.request.build_opener(cookie_processor)

    opener.open('http://www.baidu.com')

    cookiejar.save(filename=file,ignore_discard=True, ignore_expires=True)

    return opener


# 载入cookie
def load_cookie():
    file = 'cookie.txt'
    cookiejar = http.cookiejar.LWPCookieJar()
    cookiejar.load(filename=file, ignore_expires=True, ignore_discard=True)

    cookie_processor = urllib.request.HTTPCookieProcessor(cookiejar)
    opener = urllib.request.build_opener(cookie_processor)

    response = opener.open('http://www.baidu.com')

    return response



# 获取人人网cookie
def loggin_renren():
    cookiejar = http.cookiejar.CookieJar()
    cookie_processor = urllib.request.HTTPCookieProcessor(cookiejar)
    opener = urllib.request.build_opener(cookie_processor)
    opener.handlers = ["User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"]

    login_url1 = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018551146707 '
    data = {
        'email': '17688166224',
        'password': 'l2l8tc..'
    }
    data = bytes(urllib.parse.urlencode(data), encoding='utf-8')
    request = urllib.request.Request(login_url1, data = data)

    opener.open(request)

    response = opener.open('http://www.renren.com/966471588')

    print(response.read().decode())



# 使用cookie登陆51zixue
def login_51zixue():
    cookiejar = http.cookiejar.CookieJar()
    cookie_processor = urllib.request.HTTPCookieProcessor(cookiejar)
    opener = urllib.request.build_opener(cookie_processor)

    data = {
        'username': '司马小亮',
        'password': 'l2l8tc..'
    }

    data = bytes(urllib.parse.urlencode(data), encoding='utf-8')

    url = 'http://www.51zxw.net/bbs/login.asp?action=chk '
    request = urllib.request.Request(url,data=data)

    res = opener.open(request)
    print(res.read().decode('gb2312'))

    return 0


# 数据可视化  / 中文问题未解决
def use_maplotlib():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    # matplotlib.rcParams['font.sans-serif']=['文泉驿等宽正黑']
    # matplotlib.rcParams['font.family'] = 'Medium,中等'
    #
    # 设置自定义的中文字体
    myfont = FontProperties(fname="/usr/share/fonts/chinese/文泉驿等宽正黑.ttf")
    logger.debug(type(myfont))
    # 防止-号等乱码
    matplotlib.rcParams['axes.unicode_minus'] = False

    plt.title('中文测试',fontproperties = myfont)

    plt.bar([1], [10], label = "guangdong")
    plt.bar([2], [3], label = 'guangxi')
    plt.bar([3], [7], label = 'xiangang')

    plt.bar([4], [11], label = '西藏')

    plt.legend()  # 绘制
    plt.show()
    plt.savefig('hello22.png')



# jieba
def use_jieba():
    import jieba
    str = '今天天气真是不错'
    word_list = jieba.cut(str, cut_all=True)  # generator
    word_list = ' '.join(word_list)
    logger.debug(type(word_list))
    print(word_list)


# 创建词云
def create_wordcloud():
    import numpy as np
    import jieba
    from PIL import Image
    from wordcloud import ImageColorGenerator, WordCloud, STOPWORDS
    import matplotlib.pyplot as plt
    file = open('1.txt').read()
    words = jieba.cut_for_search(file)
    word_list = 'print'.join(words)
    ndarray = np.array(Image.open('3.png'))
    ndarray2 = np.array(Image.open('2.png'))

    # 下载图片
    def dowload_image():
        image = urllib.request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1529145136299&di=caca80e22adbc8b7596e96eff8f7eba2&imgtype=0&src=http%3A%2F%2Fwww.3987.com%2Farticle%2FUploadPic%2F2011-3%2F201137121056641.jpg',filename='5.jpg')
        return image
    dowload_image()
    ndarray3 = np.array(Image.open(dowload_image()[0]))
    word_cloud = WordCloud(background_color='white',
                           mask=ndarray3, # 根据ndarray的色彩形状生成文字的排列形状
                           max_words=20,
                           stopwords=STOPWORDS,
                           font_path='文泉驿等宽正黑.ttf',
                           max_font_size=200,
                           random_state=50,
                           color_func=ImageColorGenerator(ndarray3),  # 设置词云中文字的颜色
                           scale=20).generate(word_list)

    logger.debug(type(word_cloud))
    plt.imshow(word_cloud)
    plt.axis('off')  # 隐藏plt的原有图形显示内容
    plt.savefig('wordclud8.png')
    pass


# 词云-任务形状
def alice():

    pass


if __name__ == '__main__':
    create_wordcloud()
    pass

