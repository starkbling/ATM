#-*- coding:utf-8 -*-
"""
__author__ = Bling
"""
class Settings():
    """用来设置基本的用户信息"""
    def __init__(self):
        self.credit_limit = 15000
        self.bill_day = 22
        self.cash_rate = 0.05
        self.product_list ={"Bicycle":500,"Bag":80,"Glasses":100,"Chocolate":10,"Computer":9000}
        self.user_status = False
        self.atm_status = False
        self.atm_count = {"a":200000,"b":10000,"c":15000,"d":30000}
        self.atm_users = {"a":"111","b":"222","c":"333","d":"444"}