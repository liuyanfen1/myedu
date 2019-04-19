def test1_lyf1():
    print('test1')
    # print('test')
def test2_lyf2():
    print('test2')
def test3_lyf3():
    print('test3')
def int_demo():
    # 声明一个变量，变量=变量值
    aint = 5
    # 打印aint变量
    print(aint)
    # 打印变量类型
    print(type(aint))
def string_demo():
    astr = '5'
    print(astr)
    print(type(astr))

def flaot_demo():
    afloat = 0.11
    print(afloat)
    print(type(afloat))


def type_zhuanghuan():
    aint = 8
    print(type(str(aint)))
    print(type(int(aint)))

def str_join():
    a = 456
    b = '哈喽'
    c = 0.11
    print('%s %s %s'%(a,b,c))
    print('a是%s b是%s c是%s'%(a,b,c))

def jianfa_demo(a,b):
    c = a-b
    return c
def add_demo(a,b):
    print(a+b)



if __name__ == '__main__':
    # test3_lyf3()
    # test1_lyf1()
    # test2_lyf2()
    # int_demo()
    # string_demo()
    # flaot_demo()
    # add_demo(465664,57987954654)
    # add_demo('你好','123')
    # type_zhuanghuan()
    # str_join()
    # add_demo()
    c = jianfa_demo(6, 2)
    print(c)
    d = add_demo(6, 2)
    print(d)
    print(type(d))
