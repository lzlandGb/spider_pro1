#!/usr/local/python3/bin/python3
import os


from Tools.tools import debug_log


logger = debug_log(os.getcwd())
file = open('nasa2.txt', 'r')

filelines = file.readlines()



mylist = []
for line in filelines:

    line = line.split('\t')
    if len(line) < 2:
        continue
    if not isinstance(line, list):
        continue
    try:
        print(eval(line[3]))
        mylist.append(line)
    except:
        logger.debug("年龄不合法")


'''
mylist.sort(key=lambda x: eval(x[3]))
mylist.reverse()

# 年龄排序
savafile = open('savedesc2.txt', 'w')
for data in mylist:
    savafile.write(str(data)+'\t\n')
'''



# 学历排序

def level_num(xueli):
    if xueli == '大专':
        return 1
    elif xueli == '本科':
        return 2
    elif xueli == '研究生':
        return 3
    elif xueli == '硕士':
        return 4
    elif xueli == '博士':
        return 5
    else:
        return 0
mylist.sort(key=lambda x:level_num(x[5]))
savefile2 = open('xueli.txt','w')
for data in mylist:
    savefile2.write(str(data)+'\t\n')

file.close()