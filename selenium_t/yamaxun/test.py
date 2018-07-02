import re

str = 'sadfahello python'

restr = '(he.*o)'

print(re.search(restr, str))