import urllib.request
import os


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='get_picture.log')

def get_picture():
    response = urllib.request.urlopen("https://mp.weixin.qq.com/s/MevhhvosfM3Q9SRaUtpN4Q")
    print(dir(response))
    print(response.read().decode('utf-8'))


def get_picture_with_requests():
    import requests
    response = requests.get('https://mp.weixin.qq.com/s/MevhhvosfM3Q9SRaUtpN4Q', verify = False)
    print(response.text)


# 使用selenium
def get_picture_with_selenim():
    import selenium.webdriver

    url = 'https://mp.weixin.qq.com/s/MevhhvosfM3Q9SRaUtpN4Q'
    driver = selenium.webdriver.PhantomJS()
    driver.get(url)

    # picture_span_elems = driver.find_elements_by_xpath("//span[@style='font-size: 15px;']//img/")
    # picture_p_elems = driver.find_element_by_xpath("//p[@style='line-height: 25.6px;white-space: normal;text-align: center']")
    picture_elems = driver.find_elements_by_xpath("//img[@data-type='jpeg']")

    picture_urls = []
    for u in picture_elems:
        picture_urls.append(u.get_attribute('data-src'))

    # 数据流与io流分离
    i = 1
    for u in picture_urls:
        urllib.request.urlretrieve(u, os.getcwd() + '/' + str(i) + '.jpeg')
        logger.debug('第' + str(i) + '张图片下载完成')
        i += 1

    logger.debug('全部图片下载完毕')



if __name__ == '__main__':
    # get_picture()
    # get_picture_with_requests()
    get_picture_with_selenim()