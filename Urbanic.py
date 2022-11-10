import mysql.connector as py 
import random as ram
import pywhatkit
mydb = py.connect(
    host="localhost",
    user="root",
    passwd="{Enter Yours}",
    database = "StockBillSystem",
)
productdet = []
mycursor = mydb.cursor()
while True:
    def createDB ():
        formula = "CREATE DATABASE StockBillSystem"
        mycursor.execute(formula)
        print("DB Created")
    # createDB()

    def createTable ():
        # formula = "CREATE TABLE products(pro_name VARCHAR(255),product_id INT(255),product_price INT(10),stock INT(9))"
        formula = "CREATE TABLE bill(name VARCHAR(255),phone_no VARCHAR(11),Items VARCHAR(255),Item_quantiy INT,amt INT,tax INT,total INT)"
        mycursor.execute(formula)
        print("Table Created")
    #Product Table created
    # createTable() 

    #bill Table created
    # createTable() 
    whatTodo = input("Add Product Or Make Bill \n For Bill type Make \n For Product type Add\nFor Adding Stock Type Stock\nFor Getting Bill Of 1 Person type Get1:")

    def InsertProduct (name , id ,price,stock):
        name1  = name
        id1  = id
        price1  = price
        stock1  = stock
        formula = "INSERT INTO products(pro_name,product_id,product_price,stock) VALUES (%s,%s,%s,%s)"
        data = (
            name1,
            id1,
            price1,
            stock1
        )
        mycursor.execute(formula,data)
        mydb.commit()
        print("Product Added")
    def AddBill (name ,phone,items,itemq):
        itemss = items
        names = name
        print(names)
        get = "SELECT * FROM products WHERE pro_name = %s"
        # da = (items)
        mycursor.execute(get,(itemss, ))
        myresult=mycursor.fetchall()
        if myresult == []:
            print("Product Not Found")
        else:
            for detail in myresult:
                # print(detail)
                for det in detail:
                    productdet.append(det)
                    
        if productdet[3] == 0:
            print("Sorry There Is No Stock")
            
        else:
            formula = "INSERT INTO bill(name,phone_no,Items,Item_quantiy,amt,tax,total) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            amt = productdet[2]*itemq
            tax = amt/50
            total=amt+tax
            data = (
                name,
                phone,
                productdet[0],
                itemq,
                amt,
                tax,
                total,

            )
            mycursor.execute(formula,data)
            mydb.commit()

            formula = "UPDATE products SET stock = %s WHERE product_id = %s"
            dataa = (
                productdet[3]-itemq,
                productdet[1]
            )
            mycursor.execute(formula,dataa)
            mydb.commit()
            print("Bill Made")
            print("BILL")
            print(f"name        {name}")
            print(f"phone        {phone}")
            print(f"item name        {items}")
            print(f"Item Quantity        {itemq}")
            print(f"Amount        {amt}")
            print(f"Tax        {tax}")
            print(f"Total        {total}")
            import datetime

            x = datetime.datetime.now()

            bill = f"Bill\nname        {name}\nphone        {phone}\nitem name        {items}\nItem Quantity        {itemq}\nAmount        {amt}\nTax        {tax}\nTotal        {total}"

            file = open(f"./Bills/{phone}.txt","a")
            file.write(f"\n{x}\nname        {name}\nphone        {phone}\nitem name        {items}\nItem Quantity        {itemq}\nAmount        {amt}\nTax        {tax}\nTotal        {total}\n")
            
    def addStock(name,stock):
        get = "SELECT * FROM products WHERE pro_name = %s"
        # da = (items)
        mycursor.execute(get,(name, ))
        myresult=mycursor.fetchall()
        if myresult == []:
            print("Product Not Found")
        else:
            for detail in myresult:
                # print(detail)
                for det in detail:
                    productdet.append(det)
            formula = "UPDATE products SET stock = %s WHERE pro_name = %s"
            dataa = (
                productdet[3]+stock,
                name
            )
            mycursor.execute(formula,dataa)
            mydb.commit()
            print("Stock has been Added")
    def Get1(ph):
        formula = "SELECT * FROM bill WHERE phone_no = %s"
        mycursor.execute(formula,(ph, ))
        myresult = mycursor.fetchall()
        for data in myresult :
            print(data)
    if whatTodo == "Make":
        name1 = input("Enter Your Name:\n")
        phone = int(input("Enter Your Phone Number:\n"))
        item = input("Enter The Product Name:\n")
        itemq = int(input("Enter Quantity:\n"))
        AddBill(name1,phone,item,itemq) 
        
        
    elif whatTodo == "Add":
        proname = input("Enter The New Product Name:\n")
        proid = ram.randint(0,99999)
        proprice = int(input("Enter The New Product Price:\n"))
        stock = int(input("Enter The Stock We Have:\n"))

        InsertProduct(proname,proid,proprice,stock)
    elif whatTodo == "Stock":
        proname = input("Enter The  Product Name:\n")

        stock = int(input("Enter The Stock To Be Added:\n"))

        addStock(proname,stock)
    elif whatTodo == "Get1":
        phone = int(input("Enter Your Phone Number:\n"))

        Get1(phone)
    else:
        print("Please Try Again")    
