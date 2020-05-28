import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import init_DB as iDB
import seaborn as sns


def percentilsAverageRest(connection):
	cursor = connection.cursor()
	result = cursor.execute("Select Mitja from SIO.RestaurantData")
	result = cursor.fetchall()
	result_clean = []
	users = []
	for i in result:
		result_clean.append(i[0])
	df = pd.DataFrame({'Valor': tuple(result_clean)}, columns=['Valor'])
	print (df)
	print ("Percentil 10 " + str(df['Valor'].quantile(0.10)))
	print ("Percentil 25 " + str(df['Valor'].quantile(0.25)))
	print ("Mediana " + str(df['Valor'].quantile(0.50)))
	print ("Percentil 75 " + str(df['Valor'].quantile(0.75)))
	print ("Percentil 90 " + str(df['Valor'].quantile(0.90)))

	df.boxplot()
	plt.style.use('seaborn-white')
	plt.title("Diagrama de la dispersió de les mitjes dels restaurants")
	plt.show()
	df.hist(rwidth=0.97)
	plt.style.use('seaborn-white')
	plt.title("Histograma de la dispersió de les mitjes dels restaurants")
	plt.show()

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

def densitivyRest(conn, rest):
	cursor = conn.cursor()
	result = cursor.execute(f"SELECT Valoration, Restaurant_name FROM SIO.valorations v WHERE Restaurant_name = '{rest}';")
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
	print (df)
	df.plot(kind='density')
	plt.show()

def histogramaRestDesv(conn):
	cursor = conn.cursor()
	result = cursor.execute(f"SELECT Desv_pobl, Restaurant_name FROM SIO.RestaurantData v")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	valors = []
	rests = []
	for i in result:
		valors.append(i[0])
		rests.append(str(i[1]).replace('Restaurant', ''))
	# Crear el pandas dataframe
	df = pd.DataFrame({'Desv_pobl': tuple(valors),
		'Rests': tuple(rests)},
		columns = ['Desv_pobl', 'Rests'])

	plt.style.use('seaborn-white')
	df.hist(rwidth=0.97, density = True ) # Mostra la gràfica
	plt.title('Histograma de desviació estàndard per cada restaurant')
	plt.show()

def restaurantExtrems(conn):
	cursor = conn.cursor()
	result = cursor.execute(f"SELECT Desv_pobl, Mitja Restaurant_name FROM SIO.RestaurantData v \
		WHERE (Desv_pobl > 5.1 or Desv_pobl < 4.4 ) and (Mitja > 2.75 and Mitja < -3) ")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	valors = []
	rests = []
	mitja = []
	for i in result:
		valors.append(i[0])
		rests.append(str(i[1]).replace('Restaurant', ''))
		mitja.append(i[2])
	# Crear el pandas dataframe
	df = pd.DataFrame({'Desv_pobl': tuple(valors),
		'Rests': tuple(rests),
		'Mitja': tuple(mitja)},
		columns = ['Desv_pobl', 'Rests', 'Mitja'])
	aux = []
	for index, row in df.iterrows():
		aux.append(row['Rests'])
	print (aux)
	print ("Son un total de " + str(len(aux)))

def densitivyRestUser(conn, user):
	cursor = conn.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE Restaurant_name = '{user}';")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	valors = []
	rests = []
	for i in result:
		valors.append(i[0])
	# Crear el pandas dataframe
	df = pd.DataFrame({'Valor': tuple(valors)},
		columns = ['Valor'])
	print (df)
	df.plot(kind='density')
	plt.title("Densitat de les valoracions per a Restaurant1")
	df.hist(rwidth=0.97)
	plt.title("Histograma de les valoracions per a Restaurant1")
	plt.show()

conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')
densitivyRestUser(conn, 'Restaurant1')
percentilsAverageRest(conn)
dispersioRestAverage(conn)
histogramaRestAverage(conn)
histogramaRestDesv(conn)
restaurantExtrems(conn)
densitivyRest(conn, 'Restaurant1')
densitivyRest(conn, 'Restaurant2')
densitivyRest(conn, 'Restaurant3')
densitivyRest(conn, 'Restaurant4')
densitivyRest(conn, 'Restaurant5')
