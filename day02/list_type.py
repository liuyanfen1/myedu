def list_sel(a):
    print(a[2])
    print(a[0:4])
    print(a[0:])
    print(a[2:-1])

def list_sel():
    alist = ['a', 4, 'nihao', '你好', 5, 'klj', 'kadhjk']
    alist.pop()
    print(alist)
    alist.pop(3)
    print(alist)
    alist.pop(4)
    print(alist)
    blist=alist[:-2]
    print(blist)

def list_add():
    alist = ['a', 4, 'nihao', '你好', 5, 'klj', 'kadhjk']
    alist.append('haihi')
    print(alist)
    blist=[1,2,2,3,3,3]
    alist.append(blist)
    print(alist)
    clist=[1,2,3]
    alist.append(clist)
    print(alist)
def list_update():
    alist=['a', 4, 'nihao', '你好', 5, 'klj', 'kadhjk', 'haihi', [1, 2, 2, 3, 3, 3]]
    alist[0]=alist[-1]
    print(alist)

if __name__ == '__main__':
    alist =['a',4,'nihao','你好',5,'klj','kadhjk']
    # list_sel(alist)
    # list_sel()
    # list_add()
    # list_update()
    print(len(alist))