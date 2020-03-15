import pymysql
import csv
import pandas as pd
import numpy as np
import init_DB as iDB
import functions as func
import graph as gp
import matplotlib

def getMedianForRestaurant(conn, Restaurant):
	cursor = conn.cursor()
	cursor.execute(f"SELECT Valoration FROM SIO.valorations as v WHERE Restaurant_name = '{Restaurant}';")
	result = cursor.fetchall()
	df = pd.DataFrame(tuple(result), columns=['Valor'])
	df.sort_values(by='Valor')
	df = df.median()
	return (df[0])

def getAverageForRestaurant(conn, Restaurant):
	cursor = conn.cursor()
	cursor.execute(f"SELECT avg(valorations.Valoration) FROM SIO.valorations WHERE Restaurant_name = '{Restaurant}';")
	result = cursor.fetchall()
	return (result[0][0])

def getModePerRestaurant(connection, Restaurant):
	# Interval modal https://es.wikipedia.org/wiki/Moda_(estad%C3%ADstica)
	print (f"\n***\n{Restaurant}\n***")
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE Restaurant_name = '{Restaurant}'")
	result = cursor.fetchall()
	result_clean = []
	for i in result:
		result_clean.append(i[0])
	df = pd.DataFrame({'Valor': tuple(result_clean)})
	df['Valor'] = df['Valor'].apply(np.int64)
	mode = df.mode()
	return mode['Valor'][0]

def getDesvPerRestaurant(connection, Restaurant):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE Restaurant_name = '{Restaurant}'")
	result = cursor.fetchall()
	result_clean = []
	for i in result:
		result_clean.append(i[0])
	df = pd.DataFrame({'Valor': tuple(result_clean)})
	df['Valor'] = df['Valor'].apply(np.int64)
	return (df.std(axis=0)[0])

def getCountPerRestaurant(connection, Restaurant):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE Restaurant_name = '{Restaurant}'")
	return (result)

def insertDataRestaurant(conn, Restaurant, mitja, mediana, desv_pobl, moda, recompte):
	cursor = conn.cursor()
	cursor.execute(f"INSERT INTO SIO.RestaurantData (Restaurant_name, Mitja, \
		Mediana, Recompte, Desv_pobl, Moda) VALUES ('{Restaurant}', {mitja}, {mediana}, \
		{recompte}, {desv_pobl}, {moda});")
	"""
	print (f"\nRestaurant {u}\nMitja {mitja}\nMediana {mediana}\nDesv_pobl {desv_pobl} \
		\nModa {moda}\nRecompte {recompte}")
	"""
	conn.commit()

conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')

Restaurant ='Restaurant1'

cursor = conn.cursor()

for u in iDB.allRestaurants:
	mitja = getAverageForRestaurant(conn, u)
	mediana = getMedianForRestaurant(conn, u)
	desv_pobl = getDesvPerRestaurant(conn, u)
	moda = getModePerRestaurant(conn, u)
	recompte = getCountPerRestaurant(conn, u)
	mediana = getMedianForRestaurant(conn, u)
	insertDataRestaurant(conn, u, mitja, mediana, desv_pobl, moda, recompte)
	print (f"Inserted data of {u}")

cursor.execute(f"SELECT * FROM SIO.RestaurantData LIMIT 10;")




