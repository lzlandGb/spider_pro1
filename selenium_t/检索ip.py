import selenium.webdriver


def get_ips():
    url = 'https://www.kuaidaili.com/free/'
    driver = selenium.webdriver.PhantomJS()
    driver.get(url)
    ip_elems = driver.find_elements_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr")
    print(len(ip_elems))
    for ip_elem in ip_elems:
        print(ip_elem.find_element_by_xpath('./td[1]').text)
        print(ip_elem.find_element_by_xpath('./td[4]').text)
        print(ip_elem.find_element_by_xpath('./td[5]').text)


if __name__ == '__main__':
    get_ips()