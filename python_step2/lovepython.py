import os


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='lovepython.log')


# join 函数
def test_join():
    str = 'hello'
    str2 = 'python'

    str3 = ' '.join(str2)

    print(str3)


# is 和 == 的区别
def test_is():
    a = 100
    b = 100
    c = 50
    print(id(a))
    print(id(b))
    print(id(c))
    print(a is b)
    # python和java等变量赋值的方式不同，python的奇葩的地址赋值


# 深度拷贝和浅拷贝
def test_deepcopy():
    from copy import copy, deepcopy

    # copy
    a = 100
    b = 200
    c = copy(a)

    # print(c)
    # logger.debug(type(c))
    # logger.debug(id(a))
    # logger.debug(id(c))
    # logger.debug(c == a)
    # logger.debug(c is a)

    # deepcopy
    # int类型
    # c = deepcopy(a)
    # logger.debug(c)
    # logger.debug(id(a))
    # logger.debug(id(c))
    # logger.debug(a == c)
    # logger.debug(a is c)

    # list
    a = [100, 200, 300]
    c = deepcopy(a)
    # logger.debug(a)
    # logger.debug(c)
    # logger.debug(id(a))
    # logger.debug(id(c))
    # logger.debug(a == c)
    # logger.debug(a is c)

    # 函数举例
    def test_copy(value, list=[]):
        list.append(value)
        return list

    # logger.debug(test_copy(10))    # [10]
    # logger.debug(test_copy(10, [])) # [10]
    # logger.debug(test_copy(10)) # [10, 10]
    # logger.debug(test_copy('a')) # [10,10, 'a']

    #  test
    def for_test():
        a = [100, 200, 300]
        b = [a] * 10

        # 列表的变量名占一个地址，其每个元素都各占一个地址。进行*号运算时进行的是浅拷贝copy
        # logger.debug(b)
        # logger.debug(id(b))
        logger.debug(id(b[0]))
        # logger.debug(id(b[1]))
        # logger.debug(id(b[2]))
        # logger.debug(id(b[3]))
        # logger.debug(id(b[4]))
        #
        logger.debug(id(b[0][0]))
        logger.debug(id(b[0][1]))
        logger.debug(id(b[0][2]))
        #
        # logger.debug(id(b[1][0]))
        # logger.debug(id(b[1][1]))
        # logger.debug(id(b[1][2]))
        #
        # logger.debug(id(b[2][0]))
        # logger.debug(id(b[2][1]))
        # logger.debug(id(b[2][2]))

        '''打印结果
        
        [DEBUG][2018-06-19 21:34:22,537][lovepython.py][for_test][81][[[100, 200, 300], [100, 200, 300], [100, 200, 300], [100, 200, 300], [100, 200, 300], [100, 200, 300], [100, 200, 300], [100, 200, 300], [100, 200, 300], [100, 200, 300]]]
        [DEBUG][2018-06-19 21:34:22,537][lovepython.py][for_test][82][140575312026184]
        [DEBUG][2018-06-19 21:34:22,537][lovepython.py][for_test][83][140575312026440]
        [DEBUG][2018-06-19 21:34:22,537][lovepython.py][for_test][84][140575312026440]
        [DEBUG][2018-06-19 21:34:22,537][lovepython.py][for_test][85][140575312026440]
        [DEBUG][2018-06-19 21:34:22,537][lovepython.py][for_test][86][140575312026440]
        [DEBUG][2018-06-19 21:34:22,538][lovepython.py][for_test][87][140575312026440]
        [DEBUG][2018-06-19 21:34:22,538][lovepython.py][for_test][89][9215264]
        [DEBUG][2018-06-19 21:34:22,538][lovepython.py][for_test][90][9218464]
        [DEBUG][2018-06-19 21:34:22,538][lovepython.py][for_test][91][140575466070640]
        [DEBUG][2018-06-19 21:34:22,538][lovepython.py][for_test][93][9215264]
        [DEBUG][2018-06-19 21:34:22,538][lovepython.py][for_test][94][9218464]
        [DEBUG][2018-06-19 21:34:22,538][lovepython.py][for_test][95][140575466070640]
        [DEBUG][2018-06-19 21:34:22,538][lovepython.py][for_test][97][9215264]
        [DEBUG][2018-06-19 21:34:22,538][lovepython.py][for_test][98][9218464]
        [DEBUG][2018-06-19 21:34:22,538][lovepython.py][for_test][99][140575466070640]
        
        '''
        # 由于列表元素是通过浅拷贝得来，当对其中一个元素改变时，其他copy影子元素也跟着改变
        # logger.debug(b[1].append(999))
        # logger.debug(b.append(666))
        # logger.debug(b)

        c = copy(b)
        # 由于列表的列表名占独立的地址，b 和 c的地址并不相等
        # logger.debug(id(b)) # 140557556378184
        # logger.debug(id(c)) # 140557556378376

        # c 的值等同于b
        # logger.debug(c[1])
        # logger.debug(c[1].append(999))
        # logger.debug(c.append(666))
        # logger.debug(c)

        # c的元素地址和b的元素地址是一样的
        logger.debug(id(c[0]))
        # logger.debug(id(c[1]))
        # logger.debug(id(c[2]))
        # logger.debug(id(c[3]))
        #
        logger.debug(id(b[0][0]))
        logger.debug(id(b[0][1]))
        logger.debug(id(b[0][2]))
        #
        # logger.debug(id(b[1][0]))
        # logger.debug(id(b[1][1]))
        # logger.debug(id(b[1][2]))

        deepcopy
        d = deepcopy(b)
        # logger.debug(id(b))
        # logger.debug(id(d))

        # 虽然是深拷贝，但是继承了原来元素的地址特性，即
        # logger.debug(id(d[0]))
        # logger.debug(id(d[1]))
        # logger.debug(id(d[2]))
        # logger.debug(id(d[3]))
        # logger.debug(id(d[4]))

        logger.debug(id(d[0]))
        logger.debug(id(d[0][0]))
        logger.debug(id(d[0][1]))
        logger.debug(id(d[0][2]))

    # for_test()
    test_is()


# reange()
def range_test():
    t = range(10)
    print(type(t))

if __name__ == '__main__':
    range_test()