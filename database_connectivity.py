import mysql.connector as my
con=my.connect(host = "localhost",user = "root", password="", database="tnp_student")
cur =con.cursor()
name=input("enter your name :")
city=input("enter your city :")
sql ="insert into student_info(name,city)values(%s,%s)"
val=(name,city)
cur.execute(sql,val)
con.commit()
