import time
import os


import selenium.webdriver
from selenium.webdriver.common.keys import Keys

'''
点击元素无法找到

'''

def download_file():
    driver = selenium.webdriver.PhantomJS()
    driver.get('https://pypi.org/project/selenium/#history')
    time.sleep(6)
    file_elm = driver.find_element_by_class_name('package-header__right')
    driver.save_screenshot(os.getcwd() + '/selenium_download_file.png')

    time.sleep(2)
    file_elm.click()
    # driver.save_screenshot(os.getcwd() + '/selenium_download_file.jpg')
    # 文件下载不提示配置

    # 下载
    # driver.save_screenshot(os.getcwd() + '/selenium_download_file.jpg')
    # time.sleep(1)
    # driver.find_element_by_partial_link_text('tar.gz').click()


if __name__ == '__main__':
    download_file()