#!/usr/local/python3/bin/python3

from lxml import etree
import os


from Tools.tools import debug_log


logger = debug_log(os.getcwd(),name='lxml.log')

html='''
<html>
<title> This is Title </title>
<body>
	<h1> This is h1 </h1>
	<div> This is fisrt div </div>
	<div id="divid">
		<img src="1111.png"/>
		<span id="sp1"> desc 1111.png </span>

		<img src="2222.png"/>
		<span id="sp2"> desc 2222.png </span>

		<p>
			<a href="http://www.xxxxx.com/"> link-of-xxxxxx </a>
		</p>

		<a href="http://www.yyyyyyy.com/"> link-of-yyyyyyyyy </a>
		<br/>
		<a href="http://www.zzzzzzz.com/"> link-of-zzzzzzzzz </a>

	</div>

	<p class="p_classname"> This is p with class name </p>

	<div class="div_classname"> This is div with class name </div>
	<div id = 'test'></div>

</body>
</html>
'''
def get_page_source(url=None):
    import selenium
    import selenium.webdriver
    driver = selenium.webdriver.PhantomJS()
    try:
        driver.get(url)

        return driver.page_source
    except selenium.common.exceptions.WebDriverException as e:
        logger.debug(e)
        logger.debug('网页请求错误')
        return None


if __name__ == '__main__':
    xpath = "//table[@class='newlist']//td[@class='zwmc']//a[@style='font-weight: bold']/text()"
    page_source = get_page_source('https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python&sm=0&p=1')
    html = etree.HTML(page_source)

    name_list = html.xpath("//table[@class='newlist']//td[@class='zwmc']//a[@style='font-weight: bold']/text()")

    for name in name_list:
        print(name)