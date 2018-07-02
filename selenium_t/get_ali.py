import time


import selenium.webdriver
from selenium.webdriver.common.keys import Keys

def get_ali():
    driver = selenium.webdriver.PhantomJS()
    driver.get("https://job.alibaba.com/zhaopin/positionList.htm#page/1")

    # 搜索
    search_elem = driver.find_element_by_id('keyword')
    search_elem.send_keys('android')


    search_btn = driver.find_element_by_class_name('search-btn')
    search_btn.send_keys(Keys.RETURN)
    time.sleep(10)
    print(driver.page_source)

    # 点击下一页
    # time.sleep(5)
    # next_elem = driver.find_element_by_xpath("//div[@id='J-pagination']/div[@class='pagination']/ul/li[last()]/a")
    # next_elem.click()
    # time.sleep(5)
    # print(driver.page_source)
    # driver.close()


if __name__ == '__main__':
    get_ali()