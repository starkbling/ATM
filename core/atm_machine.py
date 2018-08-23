#-*- coding:utf-8 -*-
"""
__author__ = Bling
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import settings
import time
from login import atm_login

atm_set = settings.Settings()
class Atm():
    def __init__(self,user):
        self.credit = atm_set.atm_count[user]
        self.bill_time = atm_set.bill_day
        self.cash_rate = atm_set.cash_rate
        # self.user_count = atm_set.atm_count

    @atm_login
    def pay_bill(self,cost):
        self.credit -= cost
        print("You have %s$ left."%self.credit)
        return  self.credit

    @atm_login
    def send_bill(self):
        send = (input("Do you want us to send you this month bill? yes/no")).lower()
        mday = time.localtime().tm_mday
        if mday%self.bill_time == 0 or send == "yes":
            print("Send Bill paper")

    @atm_login
    def withdraw(self):
        cash = float(input("You have %s left, how much do you want to draw? :"%self.credit))
        if cash < self.credit:
            charge = float(cash)*self.cash_rate
            self.credit -= charge + cash
            print("You have draw %s,charge %s, %s left."%(cash,charge,self.credit))
            return self.credit,charge
        else:
            print("Sorry the most you can draw is %s"%self.credit)

    @atm_login
    def payoff(self):
        payoff = input("How much do you want to refund? :")
        self.credit = self.credit + payoff
        return self.credit

    @atm_login
    def transfer(self):
        user_count = atm_set.atm_count
        receiver = input("Which count do you want to transfer money? :")
        amount = float(input("Your balance is %s$,how munch do you want to transfer? :"%self.credit))
        if amount < self.credit and receiver in user_count:
            self.credit = self.credit - amount
            user_count[receiver] = user_count[receiver] - amount
            print("Transfer successful! %s$ left."%self.credit)
        else:
            print("You don't have enough money or receiver %s is not exit."%receiver)
        return self.credit


# aa =Atm()
# aa.pay_bill(100)