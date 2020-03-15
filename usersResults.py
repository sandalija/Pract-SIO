import pymysql
import csv
import pandas as pd
import numpy as np
import init_DB as iDB
import functions as func
import graph as gp
import matplotlib


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
	return (result[0][0])

def getModePerUser(connection, user):
	# Interval modal https://es.wikipedia.org/wiki/Moda_(estad%C3%ADstica)
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE User_name = '{user}'")
	result = cursor.fetchall()
	result_clean = []
	for i in result:
		result_clean.append(i[0])
	df = pd.DataFrame({'Valor': tuple(result_clean)})
	df['Valor'] = df['Valor'].apply(np.int64)
	mode = df.mode()
	return mode['Valor'][0]

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
	cursor.execute(f"INSERT INTO SIO.UserData (User_name, Mitja, \
		Mediana, Recompte, Desv_pobl, Moda) VALUES ('{user}', {mitja}, {mediana}, \
	{recompte}, {desv_pobl}, {moda});")
	"""print (f"\nUser {u}\nMitja {mitja}\nMediana {mediana}\nDesv_pobl {desv_pobl} \
		\nModa {moda}\nRecompte {recompte}")
	"""
	conn.commit()

conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')

user ='User1'

iDB.__getUsersName__(conn, 'SIO', 'valorations')

cursor = conn.cursor()

for u in iDB.allUsers:
	mitja = getAverageForUser(conn, u)
	mediana = getMedianForUser(conn, u)
	desv_pobl = getDesvPerUser(conn, u)
	moda = getModePerUser(conn, u)
	recompte = getCountPerUser(conn, u)
	mediana = getMedianForUser(conn, u)
	insertDataUser(conn, u, mitja, mediana, desv_pobl, moda, recompte)
	print (f"Inserted data of {u}")

cursor.execute(f"SELECT * FROM SIO.UserData LIMIT 10;")




