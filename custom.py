import datetime
import sqlite3
connection = sqlite3.connect("doi.db")
cursor=connection.cursor()
connection.commit()
from update import Update
D_update = Update()


class customer:
    def run(self):
        
        print("----------------------------Welcome to Customer Section----------------------------\n")
        print("____________________________Customer Declaration Form______________________________\n")
        print("Any personal data collected on this form may be used for covid 19 track and trace \ndata processing and recoed keeping in accoedance with Government Regulations.\n You are declaring on behalf your entire booking group.")

        #getting the phone number
        PhoneNo = input("Enter your phone number = ")
        while True:
            if(len(PhoneNo)==10):
                break
            else:
                PhoneNo = input("Wromg !\nEnter your phone number = ")

        # Reading the number list
        cursor.execute("select phoneNo from details")
        numList = cursor.fetchall()

        nl =[]
        for da in numList:
            nl.append(da[0])


   
        if(PhoneNo in nl):
                   
            cursor.execute("select * from details where phoneNo=PhoneNo")
            items = cursor.fetchall()           
            detailList=list(items[0])            
            print("Date and time:\t" + str(datetime.datetime.now()))
            print("First Name:\t" + str(detailList[1]))
            print("Last Name:\t" + str(detailList[2]))
            print("Permenent Address:\t" + str(detailList[3]) +" " + str(detailList[4]) + " " + str(detailList[5]) + " " + str(detailList[6]) )
            NofPeople = input("Number of people in the group - ")         
            date = str(datetime.datetime.now())            
            cursor.execute(f"insert into entrance (phoneNo,dateTime,nofpeople) values (?, ?, ?)",(PhoneNo,date,NofPeople))
            connection.commit()
            print("----------------------------Record added sucessfully----------------------------")
            print("Hi " + str(detailList[0]) +" " + str(detailList[0]))
            print("Enter number for tasks................................\nCustomer Tasks\n 1)Type 1:Create a new bill\n 2) View Products avalable \n3)Type 0:Go back")
            ctaskNo = input("Enter number: ")
            if(ctaskNo=="1"):
                self.createaBill()
            elif(ctaskNo=="0"):
                quit()
            elif(ctaskNo=="2"):
                self.viewavalablePoducts()


        else:
           
            Fname = input("First Name:\t\t")
            Lname = input("Last Name:\t\t")
            Hno = input("house No:\t\t")
            AL1 = input("Address Line 1:\t\t")
            AL2 = input("Address Line 2:\t\t")
            AL3 = input("Address Line 3:\t\t")
            NofPeople = input("Number of people in group:\t\t")
            cursor.execute(f"insert into details (PhoneNo,Fname,Lname,Hno,AL1,AL2,AL3) values (?, ?, ?,?, ?, ?,?)",(PhoneNo,Fname,Lname,Hno,AL1,AL2,AL3))
            connection.commit()         
            date = datetime.datetime.now()
            cursor.execute(f"insert into entrance (PhoneNo,datetime,nofpeople) values (?, ?,?)",(PhoneNo,date,NofPeople))
            connection.commit()
            print("----------------------------Record added sucessfully----------------------------")

            print("Hi " + Fname + " " + Lname)
            print("Enter number for tasks................................\nCustomer Tasks\n 1)Type 1:Create a new bill\n 2) View Products avalable \n3)Type 0:Go back")
            ctaskNo = input("Enter number: ")
            if(ctaskNo=="1"):
                self.createaBill()
            elif(ctaskNo=="0"):
                quit()
            elif(ctaskNo=="2"):
                self.viewavalablePoducts()


    #method for creating the bill
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
                print("|Total (Rs) :  {:29s} |".format(str(totalPrice)))
                print("+--------------------------------------------+")
                print("|Paid amount (Rs) :  {:23s} |".format(str(paidamount)))
                print("+--------------------------------------------+")
                print("|Balance (Rs) :  {:27s} |".format(str(paidamount-totalPrice)))
                print("+--------------------------------------------+")
                print("|    Thank you caome again                   |")
                print("+--------------------------------------------+")
                break
    #method for view avalable products
    def viewavalablePoducts(self):
        
        print("+--------------------------------------------+")
        print("|{:16s}|{:14s}|{:12s}|".format("Productname","quantity","unitprice"))
        print("+--------------------------------------------+")
        prdlist = []
        cursor.execute("select * from product")
        items = cursor.fetchall()
        for i in items:
            print("|{:16s}|{:14s}|{:12s}|".format(str(list(i)[0]),str(list(i)[2]),str(list(i)[1])))
            print("+--------------------------------------------+")
                  
                        


                    






            

        


                


                





        

            
           
            

            








