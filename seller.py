import datetime
import sqlite3
connection = sqlite3.connect("doi.db")
cursor=connection.cursor()
connection.commit()
from update import Update
D_update = Update()



class Seller:
    def createaBill(self):
        cont = 1
        totalPrice=0
        paidamount=0
        Prlist=[]
        while True:
            print("->To add item press : 1\n->To place order press : *")
            pressed = input("Press : ")
            if(pressed=="1"):
                item = input("Add item {} : ".format(str(cont)))
                Qty = input("Add Qty : ")
                Prlist.append(item + " " + Qty )
                Qty = int(Qty)
                cont+=1
                value = item
                cursor.execute(f"select price from product where name='{value}'")
                items = cursor.fetchall()
                items=int(list(items[0])[0])
                totalPrice = totalPrice + (items*Qty)
                #updating the product file
                D_update.autoUpdate(item,int(Qty))
                print("__________Item added sucessfully__________")
            else:
                print("Creating Bill..........................")
                value=0
                for data in Prlist:
                    item = data
                    itemList = []
                    priceList = []
                        
                print("Total price is (Rs)\t: ",totalPrice)
                paidamount = int(input("Enter paid amount (Rs)\t: "))

                print("+--------------------------------------------+")
                print("|                FOODCITY                    |")
                print("+--------------------------------------------+")
                print("| Date :  {:35s}|".format(str(datetime.datetime.now())))
                print("+----------------+--------------+------------+")
                print("| Name           |Quantity      |Price       |")
                value = 0
             
                for data in Prlist:
                    data = data.split(" ")[0]
                    print("+----------------+--------------+------------+")
                    item = data
                    itemList = []
                    priceList = []
                    for itemin in Prlist:
                        itemList.append(itemin.split(" ")[0])                  
                    pname = data
                    cursor.execute(f"select price from product where name='{pname}'")
                    items = cursor.fetchall()
                    price=int(list(items[0])[0])
                    cursor.execute(f"select quantity from product where name='{pname}'")
                    items = cursor.fetchall()
                    quantity=int(list(items[0])[0])                   
                    print("|{:16s}|{:14s}|{:12s}|".format(pname,str(quantity),str(price)))

                    value+=1    
                print("+--------------------------------------------+")    
                print("|Total (Rs) :  {:29s} |".format(str(totalPrice)))
                print("+--------------------------------------------+")
                print("|Paid amount (Rs) :  {:23s} |".format(str(paidamount)))
                print("+--------------------------------------------+")
                print("|Balance (Rs) :  {:27s} |".format(str(paidamount-totalPrice)))
                print("+--------------------------------------------+")
                print("|    Thank you caome again                   |")
                print("+--------------------------------------------+")
                break
    #method for add new item
    def addNewitem(self):
        
        print("...............Add new item...................")
        itemName = input("Enter new product - ")

        price=0
        quantity=0

        pname = itemName
        cursor.execute(f"select price from product where name='{pname}'")
        items = cursor.fetchall()
        if(len(items)==0):
            pass
        else:
            price=int(list(items[0])[0])
            cursor.execute(f"select quantity from product where name='{pname}'")
            items = cursor.fetchall()
            quantity=int(list(items[0])[0])
            
        if(price!=0):
            qty = input("Enter quantity - ")
            up = input("Enter unit price - ")
            print("This product already in stock.\n if you want to update quantity goto 'update quantity'.")
        else:
            qty = input("Enter quantity - ")
            price = input("Enter unit price - ")
            cursor.execute(f"insert into product (name,price,quantity) values (?, ?, ?)",(pname,price,qty))
            connection.commit()
            print("New product added sucessfully..................")
    #method for update quantity
    def updateQuantity(self):
        
        print("...............Update product details...................")
        itemName = input("Enter product name - ")
        newQty = int(input("Enter Qty : "))

        U_or_not = input("Do you want to update product price - (Y/N) ")
        if(U_or_not=="Y"):
            newPrice = input("Enter unit price : (Rs) ")
            cursor.execute("UPDATE product SET price = ?, quantity = ? WHERE name = ?", (newPrice,newQty, itemName))
            connection.commit()
        else:
            cursor.execute("UPDATE product SET quantity = ?  WHERE name = ?", (newQty, itemName))
            connection.commit()

        print("..............Product stock update sucessfully...............")
    #method for get entrance records
    def getEntranceRecords(self):
        print("...........customer entrance records.............")
        number = input("Enter phone number : ")
        
        cursor.execute(f"select Fname,Lname,Hno,Al1,Al2,Al3 from details where phoneNo='{number}'")
        items = cursor.fetchall()
        connection.commit()
        print("Name : ", items[0][0], items[0][1])
        print("Permenant Address : ", items[0][2],items[0][3],items[0][4],items[0][5] )

        cursor.execute(f"select dateTime,Nofpeople from entrance where phoneNo='{number}'")
        items = cursor.fetchall()
        value=list(items[0])[0]

        print("+-----------------------------+------------------+")
        print("| Date and time               |number of group   |")
        print("+-----------------------------+------------------+")
        for i in items:
            print("|{:16s}   |{:18s}|".format(str(i[0]),str(i[1])))
            print("+----------------------------+-------------------+")


    def run(self):
        print("welcome to seller section....................")
        print("enter number to create a task................")
        print("seller tasks\n")
        print("1) Type 1: Create a new bill\n2) Type 2: Add a new product\n3) Type 3: Update Quantity\n4) Type 4: Get customer entrance records\n5) Type 0: Go back")
        num = int(input("Enter number...................."))
        if(num==1):
            self.createaBill()
        elif(num==2):
            self.addNewitem()
        elif(num==3):
            self.updateQuantity()
        elif(num==4):
            self.getEntranceRecords()
        
            
        



        


