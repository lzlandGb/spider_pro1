import selenium.webdriver
import os
import time
import re


from lxml import etree


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='login_jd.log')

def login_jd():
    login_url = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
    driver = selenium.webdriver.PhantomJS()
    driver.get(login_url)
    time.sleep(3)

    # 使用账号密码登陆
    login_form_elem = driver.find_elements_by_xpath("//div[@class='login-form']//a")
    up_elem = login_form_elem[1]
    up_elem.click()

    # 输入账号密码
    user_elem = driver.find_element_by_id("loginname")
    passwd_elem = driver.find_element_by_id("nloginpwd")



    user_elem.clear(); passwd_elem.clear()
    user_elem.send_keys('17688166224')
    time.sleep(1.2)
    passwd_elem.send_keys('l2l8tc..')

    # 在不输入验证码的情况下登陆
    time.sleep(5)
    # login_btn_div_elem = driver.find_element_by_class_name('login-btn')
    # login_btn_elem = login_btn_div_elem.find_element_by_tag_name('a')

    # 等待输入完毕
    driver.save_screenshot(os.getcwd() + '/if_login_succe.png')
    #login_btn_div_elem.click()
    driver.find_element_by_id('loginsubmit').click()
    time.sleep(2)
    driver.save_screenshot(os.getcwd() + '/if_login_succe2.png')

    # 等待一段时间查看是否登陆成功
    time.sleep(20)
    # logger.debug(driver.page_source)

    # 如果没有登陆成功，则获取验证码在此输入
    if_login_restr = '我的京东'
    if not re.search(if_login_restr, driver.page_source):
        # 验证是否有验证码
        restr = '看不清换一张'
        code_num = 1
        se_code = None
        if re.search(restr, driver.page_source):
        #     # 无论是否看的清点击切换验证码
        #     authcode_elem = driver.find_element_by_id('o-authcode')
        #     code_elem = authcode_elem.find_element_by_tag_name("a")
        #     code_elem.click()
        #     # 等待验证码切换
        #     time.sleep(5)

            # 再次输入密码登陆
            passwd_elem = driver.find_element_by_id("nloginpwd")
            passwd_elem.send_keys('l2l8tc..')
            # 等待密码输入
            time.sleep(2)

            driver.save_screenshot(os.getcwd() + '/code'+str(code_num) +'.png')
            set_code = input('请输入'+ os.getcwd()+'目录下的'+ str(code_num) + '.png 里的验证码')
            code_num += 1

        # 登陆
        if  se_code:
            authcode_elem = driver.find_element_by_id('authcode')
            authcode_elem.send_keys(se_code)
        # 等待输入验证码
        time.sleep(2)

        login_btn_div_elem = driver.find_element_by_class_name('loginsubmit')
        # login_btn_elem = login_btn_div_elem.find_element_by_tag_name('a')
        login_btn_div_elem.click()

        time.sleep(2)
        # logger.debug(driver.page_source)
        return driver
    else:
        logger.debug('成功登陆')
        return driver
    pass


def get_info():
    driver = login_jd()
    # 进入购物车
    shopping_car_div_elem = driver.find_element_by_id('settleup')
    shopping_car_elem = shopping_car_div_elem.find_element_by_tag_name('a')
    shopping_car_elem.click()

    # 使用xpath捉取购物车商品信息
    time.sleep(2)
    driver.get('https://cart.jd.com/cart?rd=0.28991924288859216')

    # 网页代码写入文本
    # with open(os.getcwd() + '/shopping_car.html', 'w') as f:
    #     f.write(driver.page_source)
    html = etree.HTML(driver.page_source)
    # s = html.xpath("//div[@class='item-list']//div[@class='item-last item-item item-selected']//div[@class='p-name']/a")
    s = html.xpath("//div[@class='goods-item']/div[@class='p-img']/a/img")
    print(len(s))
    for i in s:
        print(i.attrib.get('alt'))

if __name__ == '__main__':
    get_info()
    pass