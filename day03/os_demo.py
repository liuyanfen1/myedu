import os
if __name__ == '__main__':
    # 获取当前目录
    pwd=os.getcwd()
    print(pwd)
    # 返回上级目录的字符串
    b=os.path.abspath('..')
    print(b)
    # 返回上上级目录
    c=os.path.abspath('../..')
    print(c)