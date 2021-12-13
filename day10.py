"""
要求：
1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
4、使用新手机对象调用手机介绍的方法；
5、使用新手机对象调用打电话的方法；
"""


# class OldPhone:
#     __bank = ""
#
#     def setBank(self, bank):
#         self.__bank = bank
#
#     def getBank(self):
#         return self.__bank
#
#     def show(self, name):
#         print(self.__bank, "正在给%s打电话" % name)
#
#
# class NewPhone(OldPhone):
#     def show(self, name):
#         super().show(name)
#
#     def show1(self):
#         print("语音拨号中...")
#
# p = NewPhone()
# p.setBank("华为手机")
# p.show("李四")
# p.show1()

"""
1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
4、定义测试类，对厨师类中的姓名和年龄创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，属性赋值，并获取赋值后的属性值打印到控制台上；
5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；
"""


class Cook(object):
    __name = ""
    __age = 0

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def show(self):
        print(self.__name, "正在做饭...")


class Apprentice(Cook):
    def cook(self):
        print("正在炒菜")


class Disciple(Apprentice, Cook):
    def show(self):
        print(self.getName(),"正在做饭")

    def cook(self):
        print(self.getName(), "正在炒菜")

    def show1(self):
        print(self.getName(),
              self.getAge())


d = Disciple()
d.setName("李不白")
d.setAge(50)
d.show1()
d.show()
d.cook()