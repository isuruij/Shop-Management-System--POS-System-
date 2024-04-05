from custom import customer
from seller import Seller
cus = customer()
sel = Seller()
import sqlite3
connection = sqlite3.connect("doi.db")
cursor=connection.cursor()
connection.commit()



print("::::::::::::Welcome to FoodCity::::::::::::\n Enter number to access the system \n LOGIN\n 1)Type 1: shop management Login \n 2)Type 2: Customer Login \n 3)Type 3:Quit")
number = (input("Enter number - "))
while True:
    if(number=="1"):
        print("enter user name and password")
        username = input("enter user name - ")
        password = input("enter password - ")
        if(username=="user" and password=="user"):
            
            sel.run()
            print("inside shop magement")
        else:
            print("wrong usermane or password. Try again !")
            username = input("enter user name - ")
            password = input("enter password - ")

        print("::::::::::::Welcome to Gampaha FoodCity::::::::::::\n Enter number to access the system \n LOGIN\n 1)Type 1: shop management Login \n 2)Type 2: Customer Login \n 3)Type 3:Quit")
        number = (input("Enter number - "))
    elif(number=="2"):
        cus.run()
        
        print("::::::::::::Welcome to Gampaha FoodCity::::::::::::\n Enter number to access the system \n LOGIN\n 1)Type 1: shop management Login \n 2)Type 2: Customer Login \n 3)Type 3:Quit")
        number = (input("Enter number - "))
    elif(number=="3"):
        quit()
    else:
        print("invalied Input")
        print("::::::::::::Welcome to Gampaha FoodCity::::::::::::\n Enter number to access the system \n LOGIN\n 1)Type 1: shop management Login \n 2)Type 2: Customer Login \n 3)Type 3:Quit")
        number = (input("Enter number - "))

