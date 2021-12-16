import time
from threading import Thread

bag = 500
money = 30000


class Cook(Thread):
    name = ''
    count = 0
    salary = 0

    def run(self) -> None:
        global bag

        while True:
            if bag > 0:
                self.count += 1
                bag -= 1
                self.salary = self.count * 1.5
                print(self.name, "做了",self.count,"个蛋糕,工资:",self.salary)
                time.sleep(0.01)
            else:
                # print(self.name, "总共做了", self.count, "个蛋糕")
                break


class Customer(Thread):
    name = ''
    num = 0

    def run(self) -> None:
        global money
        while True:
            if money > 0:
                if bag > 0:
                    self.num += 1
                    money -= 3
                    print(self.name, "抢了", self.num, "个蛋糕, 剩余money:", money)
                    time.sleep(0.1)
                else :
                    # print("蛋糕抢完了")
                    break


c1 = Cook()
c2 = Cook()

c3 = Customer()
c4 = Customer()

c1.name = "张三"
c2.name = '李四'

c3.name = '王五'
c4.name = '赵四儿'


c1.start()
c2.start()

c3.start()
c4.start()