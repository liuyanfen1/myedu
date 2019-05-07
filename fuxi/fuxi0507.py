# 题：新建一个list变量，里面有五个元素，访问索引2，切片1-4，删除索引3，添加两个元素，第0位元素改成字符5，获取索引长度
def list_del():
    alist = [1, 'haha', 3, 4, 5]
    print(alist[1])
    print(alist[0:3])
    alist.pop(alist[2])
    print(alist)
    alist.append(7)
    alist.append(8)
    alist[1]=5
    print(alist)
    print(len(alist))
# 新建一个字典变量，里面有两个键值对，访问一个值，删除一个键值对，添加一个键值对，更改任意一个值，再新建一个字典，将两个合并
adict = {'1' :'lyf', '2' : '123456'}
bdict = {'5':'www','password':'789456'}
def adict_sel():
    print(adict['1'])
    adict.pop('1')
    print(adict)
    adict['3']='456789'
    print(adict)
    adict['2']='username'
    print(adict)
    # 合并方式一
    adict.update(bdict)
    print(adict)
    # 合并方式二
    d=dict(adict,**bdict)
    print(d)
#  九九乘法表
def jiujiu():
    for i in range (1,10):
        for j in range(1,i+1):
            print('%s*%s=%s'%(j,i,j*i),end=' ')
        print('')

# 冒泡排序
def maopao_demo():
    alist=[2,5,6,7,9,1,8]
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j]<=alist[j+1]:
                    continue
            temp=alist[j]
            alist[j]=alist[j+1]
            alist[j+1]=temp
    print(alist)
if __name__ == '__main__':
    # list_del()
    # adict_sel()
    # jiujiu()
    maopao_demo()