import mysql.connector as a
con = a.connect(host="localhost",user="root",passwd="12345")

c = con.cursor()
sql1="create database classs"
c.execute(sql1)
sql2="use classs"
c.execute(sql2)
sql3="create table books(bname varchar(50),bcode varchar(10),total int,subject varchar(50))"
c.execute(sql3)
sql4="create table issue(bname varchar(50),regno varchar(10),bcode int,issue varchar(50))"
c.execute(sql4)
sql5="create table submit(bname varchar(50),regno varchar(10),bcode int,submit varchar(50))"
c.execute(sql5)
con.commit()


