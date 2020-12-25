#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:40:34 2020
Exercise Bank account
Make a class that represents a bank account. Create four methods named set_details, 
display, withdraw and deposit.

In the set_details method, create two instance variables : name and balance. The 
default value for balance should be zero. In the display method, display the 
values of these two instance variables.

Both the methods withdraw and deposit have amount as parameter. Inside withdraw, 
subtract the amount from balance and inside deposit, add the amount to the balance.

Create two instances of this class and call the methods on those instances.
@author: sindy
"""

class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

        
    def set_details(self):
        return self.name, self.balance
        
    def display(self):
        return f"{self.name} has a balance of {self.balance}"
        
    
    def withdraw(self, amount_withdraw):        
        self.balance -= amount_withdraw
        
    
    def deposit(self, amount_deposit):
        self.balance += amount_deposit
        

client1 = BankAccount("Becky", 3200)
client2 =  BankAccount("Ben", 4254)


print(client1.set_details())
print(client1.display())

client1.withdraw(200)
print(f"you have a new balance of {client1.balance}")

client1.deposit(500)
print(f"you have a new balance of {client1.balance}")


print(client2.set_details())
print(client2.display())   
   
client2.withdraw(1224.05)
print(f"you have a new balance of {client2.balance}")
client2.deposit(225)
print(f"you have a new balance of {client2.balance}")





#class BankAccount():
#    def set_details(self, name, balance=0):
#        self.name = name
#        self.balance = balance
#    
#    def display(self):
#        return f"{self.name} has a balance of {self.balance}"
#    
#    def withdraw(self, amount_withdraw):
#        self.balance -= amount_withdraw
#
#    def deposit(self, amount_deposit):
#        self.balance += amount_deposit