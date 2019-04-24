if __name__ == '__main__':
    # w+ 覆盖
    text_io=open('test.text','w+')
    text_io.write('哈哈哈哈哈')
    # a+ 追加
    text_io=open('test.text','a+')
    text_io.write('呵呵呵呵呵呵呵')
    # r：只可读取，不能写入
    text_io=open('test.text','r')
    # readline()读取一行
    readline=text_io.readline()
    print(readline)
    # 读取所有航，返回一个list
    readlines=text_io.readlines()
    print(readline[2])