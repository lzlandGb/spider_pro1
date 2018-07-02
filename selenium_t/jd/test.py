import re
from lxml import etree


str = 'hello python'

restr = 'o'

html = etree.HTML(str)

print(dir(html))
print(html.text)
