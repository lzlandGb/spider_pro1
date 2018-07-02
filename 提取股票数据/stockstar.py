#!/usr/local/python3/bin/python3

def get_page_source(url=None):
    import selenium.webdriver
    driver = selenium.webdriver.PhantomJS()

    page_source = driver.get(url)

    return page_source

def get_element(page_source):
    from lxml import etree

    return etree.HTML(page_source)

if __name__ == '__main__':
    table_xpath = "//table[@class='trHover']//tr[@style='background-color: rgb(255, 255, 255);']"
    tr_xpath = ""
    get_page_source('')
    pass
