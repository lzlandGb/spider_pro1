import selenium.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_from_mobile():
    # 增加手机模拟设置
    mobilesettings = {'devicename': 'iPhone 6 Plus'}
    options = selenium.webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobilesettings)

    driver = selenium.webdriver.PhantomJS()

    pass

def get_from_mobile2():
    # 增加手机模拟设置
    # mobilesettings = {'devicename': 'iPhone 6 Plus'}
    # options = selenium.webdriver.ChromeOptions()
    # options.add_experimental_option('mobileEmulation', mobilesettings)

    driver = selenium.webdriver.Chrome()
    print('hello')
    driver.get('https://blog.csdn.net/brucepanit/article/details/53671091')
    print(driver.page_source)

if __name__ == '__main__':
    # get_from_mobile()
    get_from_mobile2()
    pass