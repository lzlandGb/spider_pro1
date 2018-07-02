#!/usr/local/python3/bin/python3
import re


str = 'hello python2018'

restr = '''n
(\d+)'''

src_pattern = re.compile(restr)

num_list = src_pattern.findall(str)


print(num_list)

