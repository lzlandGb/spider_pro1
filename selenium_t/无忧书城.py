import selenium.webdriver


def get_text():
    url = "http://www.51shucheng.net/kehuan/santi/santi1/174.html"
    driver = selenium.webdriver.PhantomJS()
    driver.get(url)
    data_list = driver.find_elements_by_xpath('//*')
    for data in data_list:
        print(data.text)
    pass


if __name__ == '__main__':
    get_text()