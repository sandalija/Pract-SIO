import pymysql
import csv
import pandas as pd

import init_DB as iDB
import functions as func
import graph as gp
import matplotlib

conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')

def getDataFromUsuarisView(conn):
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM SIO.Usuaris LIMIT 10")
        result = cursor.fetchall()
        print (result)

user ='User1'

iDB.__getUsersName__(conn, 'SIO', 'valorations')

def getMedianForUser(conn, user):
        cursor = conn.cursor()
        cursor.execute(f"SELECT Valoration FROM SIO.valorations as v WHERE User_name = '{user}';")
        result = cursor.fetchall()
        df = pd.DataFrame(tuple(result), columns=['Valor'])
        df.sort_values(by='Valor')
        df = df.median()
        return (df[0])

def getAverageForUser(conn, user):
        cursor = conn.cursor()
        cursor.execute(f"SELECT avg(valorations.Valoration) FROM SIO.valorations WHERE User_name = '{user}';")
        result = cursor.fetchall()
        return (result)

def getModePerUser(connection, user):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE User_name = '{user}'")
	result = cursor.fetchall()
	df = pd.DataFrame(tuple(result))
	mode = df.mode()
	return mode

def getDesvPerUser(connection, user):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE User_name = '{user}'")
	result = cursor.fetchall()
	df = pd.DataFrame(tuple(result))
	return (df.std(axis=0)[0])

def getCountPerUser(connection, user):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE User_name = '{user}'")
	return (result)

def insertDataUser(conn, user, mitja, mediana, desv_pobl, moda, recompte):


cursor = conn.cursor()
"""
for u in iDB.allUsers:
        print ("User: "+ u)
        mediana = getMedianForUser(conn, u)
        print ("mediana " + str(mediana))
        cursor.execute(f"UPDATE SIO.Usuaris SET Mediana = '{mediana}';")
        #insertMedianForUser(conn, mediana)
conn.commit()
cursor.execute(f"SELECT Mediana FROM SIO.Usuaris LIMIT 10;")
"""
u = 'User1'
mitja = getAverageForUser(conn, u)
mediana = getMedianForUser(conn, u)
desv_pobl = getDesvPerUser(conn, u)
moda = getModePerUser(conn, u)
recompte = getCountPerUser(conn, u)
print (f"Mitja {mitja}\nMediana {mediana}\nDesv_pobl {desv_pobl}\n \
        Moda {moda}\nRecompte {recompte}")

        



