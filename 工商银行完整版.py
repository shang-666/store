# author:jason
import random
import pymysql
from DBUtils import  update
from DBUtils import select
#银行库
# bank = {}
bank_name = "中国工商银行昌平支行"
bank_choice = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}  # 银行业务选项
# 开户成功的信息模板
myinfo='''
    \033[0;32;40m
    ------------账户信息------------
    账号：{account}
    姓名：{username}
    密码：{password}
    地址：
        国家：{country}
        省份：{province}
        街道：{street}
        门牌号：{door}
    账户余额：{money}
    -------------------------------
    \033[0m
'''


# 欢迎模板
welcome = '''
***********************************
*      中国工商银行账户管理系统       *
***********************************
*               选项              *
'''

welcome_item = '''*              {0}.{1}             *'''

def print_welcome():
    print(welcome,end="")
    keys = bank_choice.keys()
    for i in keys:
        print(welcome_item.format(i,bank_choice[i]))
    print("**********************************")

# 输入帮助方法：chose是打印选项
def inputHelp(chose,datatype="str"):
    while True:
        print("请输入",chose,":")
        i = input(">>>:")
        if len(i) == 0:
            print("该项不能为空！请重新输入！")
            continue
        if datatype != "str":
            return int(i)
        else:
            return i

# 判断是否存在该银行选项
def  isExists(chose,data):
    if chose in data:
        return True
    return False


# 获取随机码
def  getRandom():
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range(8):
        string =  string + li[int(random.random()* len(li))]
    return string

# 通过账号获取账户信息
def findByAccount(name):
    sql1 = "select * from users where name = %s"
    param = [name]
    data = select(sql1, param)
    if data[0][1] == name:
        return data
    return None


# 银行的开户方法
def bank_addUser(id,name,password,country,province,street,door,money):
    # 查询是否已满
    sql = "select count(*) from users"  # (5)
    param = []
    data = select(sql,param)
    if data[0][0] >= 100:
        return 3

    # 查询是否存在
    sql1 = "select * from users where name = %s"
    param1 = [name]
    data1 = select(sql1,param1)
    if len(data1) > 0:
        return 2

    # 插入数据
    sql2 = " insert into users values(%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [id,name,password,country,province,street,door,money]
    update(sql2,param2)
    return 1


# 银行的存钱方法
def bank_saveMoney(name,money):
    sql1 = "select * from users where name = %s"
    param1 = [name]
    data1 = select(sql1, param1)
    if data1[0][1] == name :
        print(data1[0][1])
        # data1[0][7] += money
        sql2 = "update users  set money = money + %s"
        param2 = [money]
        update(sql2, param2)
        return True
    return False

# 银行的查询功能
def bank_selectUser(name,password):

    uname = findByAccount(name)

    if uname != None and len(uname) != 0:
        sql = "select * from users where password =  %s"
        param = [password]
        data1 = select(sql, param, 'all')
        if password == data1[0][2]:
            for i in data1:
                print(myinfo.format(account=i[0],
                            username=i[1],
                            password=i[2],
                            country=i[3],
                            province=i[4],
                            street=i[5],
                            door=i[6],
                            money=i[7]
                            ))
        else:
            print("用户密码错误！")
    else:
        print("该用户不存在！")

# 银行的取钱功能
def bank_takeMoney(account,password,money):
    uname = findByAccount(account)
    if uname != None:
        sql = "select * from users where password =  %s"
        param = [password]
        data1 = select(sql, param, 'all')
        if data1[0][2] == password:
            if data1[0][7] < money:
                return 3
            else:
                sql1 = "update users  set money = money - %s"
                param2 = [money]
                update(sql1, param2)
                return 0
        else:
            return 2
    else:
        return 0

# 银行的转账功能
def bank_transformMoney(outputaccount,inputaccount,outputpassword,outputmoney):
    status = bank_takeMoney(outputaccount,outputpassword,outputmoney)
    if status == 1:
        return status
    elif status == 2:
        return status
    elif status == 3:
        return status

    if inputaccount != None and findByAccount(inputaccount) != None:
        bank_saveMoney(inputaccount,outputmoney)
        return 0
    else:
        return 1


# 开户方法
def  addUser():
    name = inputHelp("用户名")
    password = inputHelp("密码")
    country = inputHelp("居住地址：1.国家：")
    province =  inputHelp("省份")
    street = inputHelp("街道")
    door = inputHelp("门牌号")
    money =  inputHelp("银行卡余额","int")
    id = getRandom()

    # 调用银行的开户方法完成开户操作  返回 1 2 3
    status = bank_addUser(id,name,password,country,province,street,door,money)
    # 判断1   2   3
    if status == 1:
        sql = "select * from users where id = %s"
        param = [id]
        data = select(sql,param)
        print("恭喜开户成功！以下是您的开户信息：")
        # print(myinfo.format(account=data["account"],
        #                     username=username,
        #                     password=user["password"],
        #                     country=user["country"],
        #                     province=user["province"],
        #                     street=user["street"],
        #                     door=user["door"],
        #                     money=user["money"],
        #                     bank_name=user["bank_name"]
        #                     ))
        for i in data:
            print(myinfo.format(account=i[0],
                                username=i[1],
                                password=i[2],
                                country=i[3],
                                province=i[4],
                                street=i[5],
                                door=i[6],
                                money=i[7],
                                ))
    elif status == 2:
        print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif status == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")

# 存钱
def saveMoney():
    name = inputHelp("姓名")
    m =  inputHelp("存入的金额","int")

    flag = bank_saveMoney(name,m)

    if flag:
        print("存储成功!您的个人信息为：")
        # uname = findByAccount(account)
        # # user = bank[uname]
        # print(myinfo.format(account=uname[0][0],
        #                     username=uname[0][1],
        #                     password=uname[0][2],
        #                     country=uname[0][3],
        #                     province=uname[0][4],
        #                     street=uname[0][5],
        #                     door=uname[0][6],
        #                     money=uname[0][7]
        #
        #                     ))
        sql = "select * from users where name = %s"
        param = [name]
        data = select(sql, param)
        for i in data:
            print(myinfo.format(account=i[0],
                                username=i[1],
                                password=i[2],
                                country=i[3],
                                province=i[4],
                                street=i[5],
                                door=i[6],
                                money=i[7],
                                ))
    else:
        print("对不起，您的个人信息不存在！请先开户后再次操作！")

# 取钱
def takeMoney():
    account = inputHelp("账户")
    password =  inputHelp("密码")
    tmoney = inputHelp("取出金额","int")

    f = bank_takeMoney(account,password,tmoney)

    if f == 1:
        print("改用户不存在！")
    elif f == 2:
        print("密码错误！")
    elif f == 3:
        print("取款金额不足！")
    elif f == 0:
        print("取款成功！")
        bank_selectUser(account,password)


# 转账功能
def transformMoney():
    output = inputHelp("转出的账号")
    input = inputHelp("转入的账号")
    outputpass =  inputHelp("转出的密码")
    outputmoney = inputHelp("要转出的金额","int")

    f = bank_transformMoney(output,input,outputpass,outputmoney)

    if f == 1:
        print("转出或转入的账号不存在！")
    elif f == 2:
        print("输入密码错误！")
    elif f == 3:
        print("转账金额不足！")
    else:
        print("转账成功！")
        print("您的个人信息：")
        bank_selectUser(output,outputpass)

# 查询账户方法
def selectUser():
    name = inputHelp("姓名")
    password = inputHelp("密码")

    bank_selectUser(name, password)

# 核心程序
while True:

    print_welcome()
    chose = inputHelp("选项")
    if isExists(chose,bank_choice):
        if chose  == "1":
            addUser()
        elif chose == "2":
            saveMoney()
        elif chose == "3":
            takeMoney()
        elif chose == "4":
            transformMoney()
        elif chose == "5":
            selectUser()
        elif chose == "6":
            print("Bye,Bye您嘞！！！！")
            break
    else:
        print("不存在改选项，别瞎弄！")