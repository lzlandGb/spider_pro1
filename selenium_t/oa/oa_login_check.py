import time
import os

import selenium.webdriver

from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='oa_login.log')
# 判断是否登陆
def if_logined(username=None, passwd=None):
    try:
        login_url = 'http://demo.smeoa.com/index.php?m=&c=public&a=login'
        driver = selenium.webdriver.PhantomJS()
        driver.get(login_url)
        time.sleep(2)

        # 登陆
        username_elem = driver.find_element_by_id('emp_no')
        passwd_elem = driver.find_element_by_id('password')
        login_elem = driver.find_element_by_id('login_btn')

        username_elem.send_keys(username)
        passwd_elem.send_keys(passwd)
        login_elem.click()
        time.sleep(2)

        # 获取网页代码
        person_index_url = 'http://demo.smeoa.com/index.php?m=&c=index&a=index'
        driver.get(person_index_url)
        page_source = driver.page_source
        check_if_logined = page_source.find('退出')
        return(check_if_logined != -1)

    except TypeError as e:
        logger.debug('账号密码格式错误或为空')


