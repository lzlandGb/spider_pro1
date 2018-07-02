def fun():
    fun_list = []
    i = 0
    for n in range(6):
        def fun2(m):
            print(n)
            print(n * m)
            return m * n  # return m * 5
        # fun_list.append(fun2)
        # i += 1
        # if i == 1:
        #     break
        fun2(5)
    return fun_list

if __name__ == '__main__':
    # fun_list = fun()
    # print(fun_list[0](5))
    # fun_list[0](5)
    fun()
