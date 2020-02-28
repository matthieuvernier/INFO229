import os
import mysql.connector
import time

time.sleep(240)

print("hola1")
db_connection = mysql.connector.connect(user="info229",host=os.environ['MYSQL_HOST'],password="info229")

print("hola2")

cursor = db_connection.cursor()

cursor.execute("use info229;")

cursor.execute("CREATE DATABASE test2;")

print("ciao")

