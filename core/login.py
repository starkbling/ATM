#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import settings

atm_set = settings.Settings()
user_status = atm_set.user_status  #用户登录了就把这个改成True
atm_status = atm_set.atm_status
atm_users = atm_set.atm_users

def logger():
    global atm_status
    global atm_users
    if not atm_status:
        username_c = input("Please enter credit username:")
        password_c = input("Please enter credit password:")
        if username_c in atm_users and password_c == atm_users[username_c]:
            atm_status = True
            print("Login successful !")
            return atm_status,username_c
        else:
            print("Invalid username or password !")
            return atm_status,None
    else:
        print("You already login.")
        return atm_status,None


def shopping_login(func):
    """购物时需要先登录认证之后才能进行"""
    def wrapper(*args, **kwargs):
        username = "bling"
        password = "abc123"
        global user_status
        if user_status== False :
            username_ = input("Please enter username:")
            password_ = input("Please enter password:")
            if username == username_ and password == password_:
                print("Welcom to Supermarket, let's start shopping!")
                user_status =True
                shopping_list = func(*args, **kwargs)
                return  shopping_list
            else:
                print("Invalid username or password !")
        else:
            shopping_list = func(*args, **kwargs)
            return shopping_list
    return wrapper

def atm_login(func):
    """使用信用卡的时候需要验证"""
    def wrapper(*args, **kwargs):
        global atm_status
        global atm_users
        if  not atm_status:
            username_c = input("Please enter credit username:")
            password_c = input("Please enter credit password:")
            if username_c in atm_users and password_c == atm_users[username_c]:
                print("Login successful !")
                atm_status = True
                credit = func(*args, **kwargs)
                return credit,atm_status
            else:
                print("Invalid username or password !")
        else:
            credit = func(*args, **kwargs)
            return credit,atm_status
    return wrapper

