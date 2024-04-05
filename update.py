class Update:
    def autoUpdate(self,item,Qty):

        import sqlite3
        connection = sqlite3.connect("doi.db")
        cursor=connection.cursor()
        Qty=int(Qty)
 
        cursor.execute(f"select quantity from product where name='{item}'")
        items = cursor.fetchall()
        value=int(list(items[0])[0])
        # print(type(value))
        new_qty = value - Qty        
                
        cursor.execute(f"update product set quantity=? where name=?", (new_qty,item))
        connection.commit()

              



        
                
