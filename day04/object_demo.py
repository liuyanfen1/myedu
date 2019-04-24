class Human (object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def chifan(self):
        print('%s在吃饭'%self.name)
    def shuijiao(self):
        print('%s在睡觉'%self.name)
    def dadoudou(self):
        print('%s在打豆豆'%self.name)
class Tester(Human):
    def work(self):
        self.chifan()
        print('%s在测试'%self.name)
        self.shuijiao()

if __name__ == '__main__':
    human=Human('xx',27,'女')
    # human.chifan()
    # human.shuijiao()
    # human.dadoudou()
    tester = Tester('xx',27,'女')
    tester.work()
    print(tester.sex)