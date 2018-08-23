#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
import os
import sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import settings
from atm_machine import Atm
from login import shopping_login
import json
import time


atm_set = settings.Settings()
shopping_list = []
# credit = atm.credit
# products= atm_set.product_list


@shopping_login
def shopping(products,credit,cost_all=0):
    global shopping_list
    for key,value in products.items():
        print("%s : %s $"%(key,value))
    chose = input("Which product do you want to buy?---->")
    product = chose.lower().capitalize() #将货物名转换为标准格式
    if product not in products:
        print("The product you picked is without inventory, please pick again")
        shopping(products,credit)
    else:
        if credit > products[product]:  #判断信用卡的余额是否足够支付账单
            print(credit)
            shopping_list.append(product)
            cost = products[product]
            pay_credit_card = (input("Do you want pay the bill in credit card? Y/N")).upper()
            if pay_credit_card == "Y":
                # atm.credit = credit
                results = atm.pay_bill(cost)
                if results[1]:    #判断登录是否成功，支付是否成功
                    credit = results[0]
                    cost_all += products[product]
                    print("Totally cost is %s$ , %s$ left." % (cost_all, results[0]))
                else:
                    print("Failed to pay in credit card")
                # print("credit" ,credit)
            else:
                print("You have bill to pay!")
        else:
            print("Sorry credit facility!")
    exit_ = (input("Do you want to continue shopping? Y/N :")).upper()  #确定是否要继续购物
    if exit_ != "N":
        shopping(products, credit,cost_all)
    else:
        print("Exit shopping. Totally cost is %s$ , %s$ left."%(cost_all,results[0]))
        shopping_ = [credit,cost_all,shopping_list]
        shopping_log(shopping_)
        return credit,cost_all, shopping_list

def shopping_log(shopping_):
    date_ = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    shopping_log = {}
    if shopping_:
        shopping_log[date_]=shopping_
        f = open(path + r"/log/shopping/%s.txt"%date_, "w+", encoding="utf-8")
        # print(shopping_log)
        json.dump(str(shopping_log),f)  #这里用文件保存了下来，最好是能够建立一个简单的数据库来保存
        f.close
# shopping(products,credit,cost_all=0)