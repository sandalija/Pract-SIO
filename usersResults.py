import pymysql
import csv
import pandas as pd

import init_DB as iDB
import functions as func
import graph as gp
import matplotlib

conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')

cursor = conn.cursor()
result = cursor.execute("SELECT User_name, mitjana, Total_valorations, Desviaciopoblacional \
        FROM SIO.Usuaris LIMIT 10")
result = cursor.fetchall()
print (result)


