import selenium.webdriver
import selenium.webdriver.common.keys
import os
import time


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='selenium_baidu.log')
def click_baidu():
    driver = selenium.webdriver.PhantomJS()
    driver.get("https://www.baidu.com/")
    time.sleep(2)
    keyword_elem = driver.find_element_by_id('kw')

    keyword_elem.send_keys("python")
    driver.save_screenshot(os.getcwd() + "baidu1.png")

    # 点击
    click_elem = driver.find_element_by_id("su")
    click_elem.click()
    driver.save_screenshot(os.getcwd() + "baidu2.png")

if __name__ == '__main__':
    click_baidu()