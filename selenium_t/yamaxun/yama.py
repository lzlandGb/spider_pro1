import re
import time
import json

import selenium.webdriver


def get_picture():
    info_url = 'https://www.amazon.cn/gp/product/B07BBGJG99?ref_=plp_web_a_A1UJ8J2T38KV1U_pc_1&me=A1AJ19PSB66TGU'
    driver = selenium.webdriver.PhantomJS()
    driver.get(info_url)

    '''
    'imageGalleryData' : [{"mainUrl":"https://images-cn.ssl-images-amazon.com/images/I/816t6SBXpbL.jpg"
    ,"dimensions":[1200,1784],"thumbUrl":"https://images-cn.ssl-images-amazon.com/images/I/816t6SBXpbL.
    _AC_SX75_CR,0,0,75,75_.jpg"},{"mainUrl":"https://images-cn.ssl-images-amazon.com/images/I/61De2KYCbIL.jpg",
    "dimensions":[1000,1448],"thumbUrl":"https://images-cn.ssl-images-amazon.com/images/I/61De2KYCbIL._AC_SX75_CR,0,0,75,75_.jpg"},
    {"mainUrl":"https://images-cn.ssl-images-amazon.com/images/I/71VL6-QZ0kL.jpg","dimensions":[1000,1428],
    "thumbUrl":"https://images-cn.ssl-images-amazon.com/images/I/71VL6-QZ0kL._AC_SX75_CR,0,0,75,75_.jpg"},
    {"mainUrl":"https://images-cn.ssl-images-amazon.com/images/I/71KKi6wSSvL.jpg","dimensions":[1000,1429],
    "thumbUrl":"https://images-cn.ssl-images-amazon.com/images/I/71KKi6wSSvL._AC_SX75_CR,0,0,75,75_.jpg"}],
    
    '''
    restr = 'imageGalleryData.*'
    url_str = re.findall(restr, driver.page_source)
    print(url_str[0])
    re_url = '(https://.+jpg)'

    urls = re.findall(re_url, url_str[0])

    # # 过滤换行符
    # new_url_str = []
    # for i in url_str:
    #     i = i.replace('\n', "")
    #     new_url_str.append(i)


    # new_url_str = new_url_str[0].replace("imageGalleryData' : ", "")

    # re_url = '(https://.+jpg)'
    #
    # urls = re.findall(re_url, new_url_str)

    print(urls)
    # 获取缩略图
    # picture_div_elem = driver.find_element_by_id("imageBlockThumbs")
    # picture_elems = picture_div_elem.find_elements_by_tag_name('img')
    #
    # for p in picture_elems:
    #     print(p.get_attribute('src'))
    pass


if __name__ == '__main__':
    get_picture()
    pass
