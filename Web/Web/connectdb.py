import mysql.connector
db=mysql.connector.connect(user='root', password='@Anhquy12345' ,host='localhost')

#Query
code='CREATE DATABASE `TEST 2` '

#Run
mycursor=db.cursor()
mycursor.execute(code)