# to book uber and to know how much we have to pay for ride


from geopy.geocoders import Nominatim
import geopy.distance
import mysql.connector
import datetime
import random

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Gopi@4635", database='project')
mycursor = mydb.cursor()

now = datetime.datetime.now()

loc = Nominatim(user_agent="GetLoc")

class Ride(): 
    def __init__(self):
        print("*"*5,"BOOK YOUR BUS","*"*5)
        self.name = input("enter here your name : ")
        self.time = now.strftime("%Y-%m-%d %H:%M:%S")
        mycursor.execute(f"insert into visit(name, visit_time) values('{self.name}', '{self.time}');")
        mydb.commit()

    def check(self):
        ans = input("already have an account ?(yes/no) : ")
        if ans == "yes":
            obj.user()
        else:
            print("okay then let's get you first register")
            obj.login()

    def login(self):
        rand = random.randint(100, 10000)
        self.id_1 = "TELEP101"+str(rand)
        self.age_1 = int(input("enter you age : "))
        self.email = input("enter you E-mail : ")
        self.number = input("enter your number : ")
        mycursor.execute(f"insert into user_detail(id, name, age, email, number, reg_time) values('{self.id_1}', '{self.name}', {self.age_1}, '{self.email}', '{self.number}', '{self.time}');")
        mydb.commit()
        print(f"this is your id {self.id_1}")
        obj.book_ride()

    def user(self):
        self.id_1 = input("please enter your id : ")
        a = mycursor.execute(f"select * from user_detail where id='{self.id_1}';")
        result = mycursor.fetchall()
        print(result[0][0])
        if result[0][0]==self.id_1:
            obj.book_ride()
        else:
            print("you are not registered yet")

    def book_ride(self):
        self.day = input("enter date of your journey : ")
        self.place = input("from : ")
        self.destination = input("enter your destination : ")
        getloc1 = loc.geocode(self.place)
        getloc2 = loc.geocode(self.destination)
        lat_1 = getloc1.latitude
        lon_1 = getloc1.longitude
        lat_2 = getloc2.latitude
        lon_2 = getloc2.longitude
        coord_1 = (lat_1, lon_1)
        coord_2 = (lat_1, lon_2)
        self.total = geopy.distance.geodesic(coord_1, coord_2).km
        self.p = (self.total//1)*2.5
        try:
            mycursor.execute(f"insert into booking(id, name, place, destination, day, cost) values('{self.id_1}', '{self.name}', '{self.place}', '{self.destination}', '{self.day}', {self.p});")
            mydb.commit()
        except:
            print("something went wrong")
        obj.ticket()

    def ticket(self):
        num = 14
        name = 0
        age = 0
        place = 0
        destination = 0
        date = 0
        cost = 0
        time = 0
        print("\n***Here's your ticket***\n")
        for i in range(1):
            for i in range(num*3):
                print("-", end="")
            print("\r")
        for i in range(num//2):
            for j in range(1):
                print("||", end="")
                if name == 0:
                    a = " name : "+self.name
                    print(a, end="")
                    name+=1
                elif age == 0:
                    a = " age : "+str(self.age_1)
                    print(a, end="")
                    age+=1
                elif place==0:
                    a = " place : "+self.place
                    print(a, end="")
                    place+=1
                elif destination==0:
                    a = " destinaton : "+self.destination
                    print(a, end="")
                    destination+=1
                elif time==0:
                    a = " time : 8:00AM"
                    print(a, end="")
                    time+=1

                elif date==0:
                    a = " date : "+self.day
                    print(a, end="")
                    date+=1
                elif cost==0:
                    a = " cost : "+str(self.p)
                    print(a, end="")
                    cost+=1
            for k in range(((num*3)-len(a)-4)):
                print(" ", end="")
            for l in range(1):
                print("||", end="")

            print("\r")

        for i in range(1):
            for i in range(num*3):
                print("-", end="")


obj = Ride()
obj.check()
mydb.close()
