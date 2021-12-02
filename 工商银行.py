import random

print("===============")  # 界面显示
print("|  中国工商银行 |")
print("===============")
print("|1、开户       |")
print("|2、存钱       |")
print("|3、取钱       |")
print("|4、转账       |")
print("|5、查询       |")
print("|6、退出       |")
print("===============")
# 建立库
bank = {11111111: {'password': '123456', 'name': 123, 'country': 123, 'province': 13, 'street': 12, 'door': 12,
                   'bank_name': '工商银行', 'money': 800}}  # 存储用户信息
bank_name = '工商银行'  # 写死的银行名字


def useradd():  # 定义添加用户函数
    card_id = random.randint(10000000, 99999999)  # 随机生成的卡号
    password = input('请输入您的密码')
    name = input('请输入姓名')
    country = input('请输入国家')
    province = input('请输入省')
    street = input('请输入街')
    door = input('门牌号')
    gift = bank_add(card_id, password, name, country, province, street, door)  # 传参

    if gift == 1:
        print('成功,您的账户信息为：')
        info = '''
                    ----------中国工商银行-------------
                            1、账号：%s
                            2、密码：%s
                            3、姓名：%s
                            4、国家：%s
                            5、省份：%s
                            6、街道：%s
                            7、门牌号：%s
                            8、卡余额：%s
                    ----------------------------------        

        '''
        print(info % (card_id, password, name, country, province, street, door, bank[card_id]['money']))
    elif gift == 2:
        print('用户已存在')
    elif gift == 3:
        print('用户已满')


def bank_add(card_id, password, name, country, province, street, door):  # 添加数据
    if card_id in bank:  # 判断id是否重复
        return 2
    elif len(bank) >= 100:  # 判断是否满库
        return 3
    else:  # 插入数据
        bank[card_id] = {'password': password,
                         'name': name,
                         'country': country,
                         'province': province,
                         'street': street,
                         'door': door,
                         'bank_name': bank_name,
                         'money': 0
                         }
        return 1


def putmoney():
    card_id = int(input('请输入账号'))
    put = int(input('请输入要存的额度'))
    gift2 = money_add(card_id, put)
    if gift2 == True:
        print('存入成功，您的余额为：', bank[card_id]['money'])
    elif gift2 == False:
        print('卡号不存在')


def money_add(card_id, put):
    if card_id in bank:
        y = bank[card_id]['money']
        bank[card_id]['money'] = y + put
        return True
    else:
        return False


def takemoney():
    card_id = int(input('请输入账号'))
    password = input('请输入密码')
    gift3 = take_money(card_id, password)
    if gift3 == 1:
        print('账户不存在')
    elif gift3 == 2:
        print('密码错误')
    elif gift3 == 0:
        take = int(input('请输入要取的金额'))
        gift4 = _money(card_id, take)
        if gift4 == 0:
            print('取款成功，您的卡余额为：', bank[card_id]['money'])
        elif gift4 == 3:
            print('余额不足取款失败')


def take_money(card_id, password):
    if card_id in bank and password == bank[card_id]['password']:

        return 0
    elif card_id not in bank:
        return 1
    elif card_id in bank and password != bank[card_id]['password']:
        return 2


def _money(card_id, take):
    if take <= bank[card_id]['money']:
        y = bank[card_id]['money']
        print('您的卡余额为：', y)
        bank[card_id]['money'] = y - take
        return 0
    else:
        return 3


def transmoney():
    card_id = int(input('请输入转出账户'))
    id = int(input('请输入转入账户'))
    password = input('请输入您的密码')
    take = int(input('请输入转出金额'))
    gift5 = trans_money(card_id, id, password, take)
    if gift5 == 1:
        print('账号错误')
    elif gift5 == 2:
        print('密码错误')
    elif gift5 == 3:
        print('余额不足')
    elif gift5 == 0:
        y = bank[card_id]['money']
        x = bank[id]['money']
        bank[card_id]['money'] = y - take
        bank[id]['money'] = x + take
        print('转账成功,您的余额为：', bank[card_id]['money'])


def trans_money(card_id, id, password, take):
    if card_id not in bank or id not in bank:
        return 1
    if card_id in bank and id in bank and password == bank[card_id]['password']:
        y = bank[card_id]['money']
        if take < y:
            return 0
        else:
            return 3
    elif card_id in bank and id in bank and password != bank[card_id]['password']:
        return 2


def check():
    card_id = int(input('请输入账户'))
    password = input('请输入您的密码')
    gift6 = _check(card_id, password)
    if gift6 == 0:
        print('账号不存在')
    elif gift6 == 1:
        print('密码错误')
    elif gift6 == 2:
        print('您的账户信息为：')
        info = '''
                           ----------中国工商银行-------------
                                   1、账号：%s
                                   2、密码：%s
                                   3、姓名：%s
                                   4、国家：%s
                                   5、省份：%s
                                   6、街道：%s
                                   7、门牌号：%s
                                   8、卡余额：%s
                           ----------------------------------        

               '''
        print(info % (card_id, password, bank[card_id]['name'], bank[card_id]['country'], bank[card_id]['province'],
                      bank[card_id]['street'], bank[card_id]['door'], bank[card_id]['money']))


def _check(card_id, password):
    if card_id in bank:
        if password == bank[card_id]['password']:
            return 2
        else:
            return 1
    else:
        return 0


while True:
    cc = input('请选择服务项目')
    if cc == '1':
        print('1.开户')
        useradd()

    if cc == '2':
        print('2.存钱')
        putmoney()

    if cc == '3':
        print('3.取钱')
        takemoney()

    if cc == '4':
        print('4.转账')
        transmoney()

    if cc == '5':
        print('5.查询')
        check()

    if cc == '6':
        print('退出')
        break

