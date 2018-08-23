import os
import sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import settings
from atm_machine import Atm
from shopping import shopping
from login import  logger
import json
import time


atm_set = settings.Settings()
products= atm_set.product_list

func_dic = {1:"shopping",2:"withdraw",3:"payoff",4:"send_bill",5:"transfer"}
user = None
def func():
    """让客户根据不同的需求，输入相应的数字就能完成对应的操作"""
    username_ = logger()
    global user
    global func_dic
    if username_[0]:
        if username_[1]:
            user = username_[1]
        atm = Atm(user)
        credit = atm.credit
        print("What can I do for you ?")
        for key,value in func_dic.items():
            print(str(key)+ " : " + value.capitalize())
        try:
            service_num = int(input("Please enter the number according to which service you want :"))
            if service_num in range(1,6):
                fuc = "atm." + func_dic[service_num]
                rec = eval(fuc)()
                if service_num in [1,2]:
                    atm.credit = rec[1]
                elif service_num in [3,5]:
                    atm.credit = rec
                else:
                    pass
                fuc_list = [func_dic[service_num],atm.credit]
                func_log(fuc_list)
                return func_dic[service_num],atm.credit
            else:
                print("You entered invalid number.")
        except ValueError as e :
            print(e.value)
    else:
        print("Failed login !")
        log = (input("Do you want to login again ? yes/no :")).upper()
        if log != "NO":
            func()
        else:
            print("Exit !")

def func_log(func_log):
    date_ = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    shopping_log = {}
    if func_log:
        shopping_log[date_]=func_log
        f = open(path + r"/log/function/%s.txt"%date_, "w+", encoding="utf-8")
        # print(shopping_log)
        json.dump(str(shopping_log),f)  #这里用文件保存了下来，最好是能够建立一个简单的数据库来保存
        f.close
func()


