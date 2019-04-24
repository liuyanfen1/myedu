alist =['哈','喽','wo','de',1,2,3]
def for_demo():
    for i in range(5):
        print(i)
        print('hello kitty')
def for_demo1():
    for i in range(2,5):
        print(i)
    for j in range(12,16):
        print(j)
def for_list():
    for i in alist:
        print(i)
def for_list2():
    a=len(alist)
    for i in range(7):
        print(alist[i])
# 停止所有循环
def for_break():
    for i in range(5):
        print(i)
        if i==2:
            break
# 停止本次循环，直接到下一次循环
def for_continue():
    for i in range(5):
        print(i)
        if i==2:
            continue
        print('第%s循环'%i)
        print()

if __name__ == '__main__':
    pass
    # for_demo1()
    # for_list()
    for_list2()
    # for_break()
    # for_continue()
    # for_demo()
