import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='Raut@5530',database='BANK_MANAGEMENT')

def openAcc():
    n = input("Enter the Name: ")
    ac = input("Enter the Account Number : ")
    db = input("Enter the Date of Birth : ")
    add = input("Enter the address : ")
    cn = input("Enter the contact number : ")
    ob = int(input("Enter the Opening Balance : "))

    data1 = (n,ac,db,add,cn,ob)
    data2 = (n,ac,ob)

    sql1 = ('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2 = ('insert into amount values(%s,%s,%s)')

    x = mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)

    mydb.commit()
    print("Data inserted successfully")
    main()

def DepoAmo():
    amount = input("Enter the amount you want to deposit : ")
    ac = input("Enter the Account Number : ")

    a = 'select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()
    t = result[0]+amount

    sql = ('update amount set balance where AccNo=%s')
    d = (t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def withdrawAmount():
    amount = input("Enter the amount you want to Withdraw : ")
    ac = input("Enter the Account Number : ")

    a = 'select balance from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount

    sql = ('update amount set balance where AccNo=%s')
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()

def balEnq():
    ac = input("Enter the account number : ")

    a = 'select * from amount where AccNo=%s'
    data = (ac,)

    x = mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()

    print("Balance for account number ", ac," is ",result[-1])
    main()

def DisDetails():
    ac = input("Enter the account number : ")

    a = 'select * from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)

    main()

def CloseAccount():
    ac = input("Enter the account number : ")
    sql1 = 'delete from account where AccNo=%s'
    sql2 = 'delete from amount where AccNo=%s'

    data = (ac,)
    x = mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    main()

def main():
    print('''
                1. OPEN NEW ACCOUNT 
                2. DEPOSIT AMOUNT 
                3. WITHDRAW AMOUNT
                4. BALANCE ENQUIRY
                5. DISPLAY CUSTOMER DETAILS
                6. CLOSE AN ACCOUNT ''')

    choice = input("                ENTER THE OPERATION YOU WANT TO PERFORM : ")

    if(choice=='1'):
        openAcc()
    elif(choice=='2'):
        DepoAmo()
    elif(choice=='3'):
        withdrawAmount()
    elif(choice=='4'):
        balEnq()
    elif(choice=='5'):
        DisDetails()
    elif(choice=='6'):
        CloseAccount()
    else:
        print("INVALID COMMAND")
        main()

main()