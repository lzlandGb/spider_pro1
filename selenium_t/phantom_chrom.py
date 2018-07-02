import selenium.webdriver
import os
import time


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='qq_screen.log')
def get_qq_screen():
    driver = selenium.webdriver.PhantomJS()
    driver.get('http://www.baidu.com/')  # https://www.baidu.com/
    # time.sleep(5)
    # 截图保存
    print(dir(driver))
    driver.save_screenshot(os.getcwd() + '/biadu_screen.png')

    driver.close()
    pass


if __name__ == '__main__':
    get_qq_screen()
    pass