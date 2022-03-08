print("********Welcome to My Bank**********")

import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root"
    # db = "bank"
)

crs = conn.cursor()

crs.execute("create database if not exists bank")

crs.execute("use bank")
#
# crs.execute("""CREATE TABLE transaction  (
#   account INT AUTO_INCREMENT,
#   name VARCHAR(20) ,
#   address VARCHAR(45) ,
#   amount FLOAT ,
#   PRIMARY KEY (account))
#   """)

conn.commit()

while True:
    print("1: Create New Account")
    print("2: Update existing Account")
    print("3: For deposit amount")
    print("4: For Withdraw amount")
    print("5: See all Account")

    a = int(input("What do you want ??\n"))

    if a == 1:
        account = int(input("Enter account number:"))
        name = input("Enter name:")
        address = str(input("Enter city name:"))
        amount = int(input("Enter the amount you want to deposit"))
        data = (account, name, address, amount)
        crs.execute("""
                    Insert Into transaction values (%s,%s,%s,%s)""", args=data)
        conn.commit()

    if a == 2:
        account = input("Enter account no to update ")
        name = input("Enter the new name")
        address = input("Enter the new address")
        amount = int(input("Enter the new amount"))
        data = (name, address, amount, account)
        crs.execute("""Update transaction set 
                    name = %s, 
                    address = %s,
                    data = %s
                    where account =%s""", args=data)
        conn.commit()

    if a == 3:
        account = int(input("Enter account no in which you deposit"))
        crs.execute("Select amount from transaction where account = %s", args=account, )
        result = crs.fetchone()
        print(result)
        amount = int(input("Amount you want to deposit"))
        a = sum(result, amount)
        print(a)
        data = (a, account)
        crs.execute("""
                Update transaction set amount = %s where account = %s""", args=data)

        conn.commit()

    if a == 4:
        account = int(input("Enter account no in which you deposit"))
        crs.execute("Select amount from transaction where account = %s", args=account, )
        result = crs.fetchone()
        print(result)
        amount = int(input("Amount you want to withdraw"))
        a = (result[0] - amount)
        print(a)
        data = (a, account)
        crs.execute("""
                    Update transaction set amount = %s where account = %s""", args=data)

        conn.commit()

    if a == 5:
        crs.execute("""SELECT * from transaction""")
        result = crs.fetchall()
        print("|Account|Name\t|Address|Amount|")
        print("-------------------------------")
        for row in result:
            print("|{}\t|{}\t|{}\t|{}\t|".format(row[0], row[1], row[2], row[3]), )
            print("-------------------------------")

    else:
        break
