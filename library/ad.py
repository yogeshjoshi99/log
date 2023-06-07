import mysql.connector as a
con = a.connect(host="localhost",user="root",passwd="12345",database="classs")

def addbook():
    bn = input("ENETER BOOK NAME :")
    c = input("ENTER BOOK CODE :")
    t = input("TOTAL BOOKS :")
    s = input("ENTER SUBJECT :")
    data = (bn,c,t,s)
    sql = 'insert into books values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||<")
    print("Data Entered Successfully")
    main()

def issueb():
    n = input("ENTER NAME :")
    r = input("ENTER REG NO. :")
    co = input("ENTER BOOK CODE :")
    d = input("ENTER DATE :")
    a = "insert into issue values(%s,%s,%s,%s)"
    data =(n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print(">||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||<")
    print("BOOK ISSUED TO : ",n)
    bookup(co,-1)

def submitb():
    n = input("ENTER NAME: ")
    r = input("ENTER REG NO. :")
    co = input("ENTER BOOK CODE :")
    d = input("ENTER DATE :")
    sql ='insert into submit values(%s,%s,%s,%s)'
    data =(n,r,co,d)
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||<")
    print("BOOK SUBMITTED FROM : ", n)
    bookup(co,1)

def bookup(co,u):
    a = "select total from books where bcode = %s"
    data = (co,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "update books set total =%s where bcode =%s"
    d = (t,co)
    c.execute(sql,d)
    con.commit()
    main()

def dbook():
    ac = input("ENTER BOOK CODE :")
    sql= 'delete from books where bcode = %s'
    data =(ac,)
    c =con.cursor()
    c.execute(sql,data)
    con.commit()
    main()

def dispbook():
    sql = "select*from books"
    c = con.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("BOOK NAME : ",i[0])
        print("BOOK CODE :",i[1])
        print("TOTAL :",i[2])
        print(">||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||<")
        main()

def main():
 print("                            LIBRARY MANAGER                     ")
 print("1.ADD BOOKS IN LIBRARY")
 print("2.ISSUE BOOK")
 print("3.SUBMIT BOOK")
 print("4.DELETE BOOK FROM LIBRARY")
 print("5.DISPLAY BOOKS IN LIBRARY")
 choice = int(input("ENTER TASK NO:"))
 print(">||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||<")
 if choice == 1:
        addbook()
 elif choice == 2:
        issueb()
 elif choice == 3:
        submitb()
 elif choice == 4:
        dbook()
 elif choice == 5:
        dispbook()
 else:
        print("WRONG CHOICE..........")
 main()

def pswd():
 ps = input("ENTER PASSWORD :")
 if ps =="py123":
       main()
 else:
      print("WRONG PASSWORD :")
      pswd()
pswd()
