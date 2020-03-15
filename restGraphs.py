import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import init_DB as iDB

def dispersioRestAverage(conn):
	cursor = conn.cursor()
	result = cursor.execute(f"SELECT Mitja, Restaurant_name FROM SIO.RestaurantData v")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	valors = []
	rests = []
	for i in result:
		valors.append(i[0])
		rests.append(str(i[1]).replace('Restaurant', ''))
	# Crear el pandas dataframe
	df = pd.DataFrame({'Mitja': tuple(valors),
		'Rests': tuple(rests)},
		columns = ['Mitja', 'Rests'])

	df = df.sort_values(by='Mitja')
	print (df)	# Mostra les dades per pantalla
	plt.style.use('seaborn-white')
	df.plot(kind='scatter', y='Rests', x='Mitja') # Mostra la gràfica
	plt.title('Dispersió de mitjes per cada restaurant, ordenat de menor a major valoració')
	plt.show()

def histogramaRestAverage(conn):
	cursor = conn.cursor()
	result = cursor.execute(f"SELECT Mitja, Restaurant_name FROM SIO.RestaurantData v")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	valors = []
	rests = []
	for i in result:
		valors.append(i[0])
		rests.append(str(i[1]).replace('Restaurant', ''))
	# Crear el pandas dataframe
	df = pd.DataFrame({'Mitja': tuple(valors),
		'Rests': tuple(rests)},
		columns = ['Mitja', 'Rests'])

	plt.style.use('seaborn-white')
	df.hist(rwidth=0.97) # Mostra la gràfica
	plt.title('Histograma de mitjes per cada restaurant')
	plt.show()



conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')
histogramaRestAverage(conn)
