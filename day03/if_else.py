def if_demo():
    a=3>2
    if a:
        print('zhen')
    else:
        print('jia')
def ifel_demo():
    a=7
    if a==1:
        print('a是1')
    elif a==2:
        print('a是2')
    elif a==3:
        print('a是3')
    elif a==4:
        print('a是4')
    elif a==5:
        print('a=5')
    elif a == 6:
        print('a=6')
    else:
        print('a是%s'%a)
    print('if结束')

if __name__ == '__main__':
    if_demo()
    ifel_demo()