import selenium.webdriver
import os
import time


from Tools.tools import debug_log
from selenium.webdriver.support.select import Select

logger = debug_log(os.getcwd(), name='login_qq_mailbox.log')
def login_qq_mailbox():
    driver = selenium.webdriver.PhantomJS()
    driver.get('https://qzone.qq.com/')
    # driver.get('https://blog.csdn.net/linlu_home/article/details/78799878')
    time.sleep(3)

    #login user u and p
    '''
                element = driver.switch_to.active_element
                alert = driver.switch_to.alert
                driver.switch_to.default_content()
                driver.switch_to.frame('frame_name')
                driver.switch_to.frame(1)
                driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
                driver.switch_to.parent_frame()
                driver.switch_to.window('main')
    '''
    # driver.switch_to.frame('login_frame')
    driver.switch_to_frame('login_frame')
    # driver.switch_to.frame(driver.find_element_by_xpath("//div[@id='login_div']/iframe"))
    print(driver.page_source)

    # btn_uc_elem = driver.find_element_by_id('qlogin')
    # btn_uc_elem.click()
    pass

# 使用requests获取代码
def get_page_source():
    import requests
    response = requests.get('https://www.baidu.com/')
    page_source = response.content
    print(page_source.decode('utf-8'))

if __name__ == '__main__':
    login_qq_mailbox()
    # get_page_source()