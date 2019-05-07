
# 计算1到50之间的奇数和?
def sum_demo():
    sum=0

    for i in range(1,51):
        if i%2==1:
            sum =sum+i
    print(sum)
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
    # jiujiu()
    # sum_demo()
    maopao_demo()
