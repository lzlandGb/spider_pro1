import time

import selenium.webdriver
from selenium.webdriver.common.keys import Keys

def login_csdn():
    driver = selenium.webdriver.PhantomJS()
    driver.get("https://passport.csdn.net/account/login")
    # 跳转到登陆
    check_elem = driver.find_element_by_xpath("//div[@class='login-part']/h3/a[1]")
    check_elem.click()

    # 登陆
    time.sleep(3)
    user_elem = driver.find_element_by_id('username')
    passwd_elem = driver.find_element_by_id('password')
    user_elem.send_keys('3237651099@qq.com')
    passwd_elem.send_keys('l2l8tc..')
    login_elem = driver.find_element_by_class_name('logging')

    # click 比keys.return要好？
    # login_elem.send_keys(Keys.RETURN)
    login_elem.click()

    # 获取信息
    source_page = driver.page_source
    print(source_page)
    pass


if __name__ == '__main__':
    login_csdn()