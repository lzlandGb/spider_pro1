import urllib.request


from lxml import etree

def get_page_source():
    url = 'http://quote.stockstar.com/fund/stock.shtml'
    headers = {"User-Agent":"Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"}
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    return response.read().decode('gb2312')



if __name__ == '__main__':
    page_source = get_page_source()
    print(page_source)
    html = etree.HTML(page_source)
    xpath = "//tbody[@class='tbody_right']//tr//td//text()"
    data = html.xpath(xpath)
    print(data)