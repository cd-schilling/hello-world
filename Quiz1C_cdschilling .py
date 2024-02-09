#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:46:48 2024

@author: cadedschilling
Quiz 1C
"""
#this progrsam will help a small business manage inventory 

#first, we will ask for the name of the item from the user
item = input("Enter the item name: ")

#next, we will ask for the quantity of the item in-stock
quantity = int(input("What is the quantity of " + item + " in stock: "))

#Next, we will ask for the price
price_per_unit = float(input("Enter the price of the " + item + ": $"))

#Next, we will calculate the total value of the inventory for the item using the equation shown. 
total_value = quantity * price_per_unit

print("The total value of the inventory for that item is", total_value) 


