import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

# Fitxer amb les funcions de la pràctica

# Algunes parts estàn hardcoded, i ho hauriem d'arreglar

""" 
Les funcions acostumen a tenir el mateix esquema:
	1. A partir de la connexió del paràmetre, fa una query al MySQL
	2. Tracta les dades, a vegades com un Pandas Dataframe 
Els pandas Dataframes són estructures que permeten analitzar un conjunt de dades
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
i tenen diferents mètodes per a calcular mitjanes, desviacions, .. i inclós gràfics
"""


# Retorna la cantidad de valoraciones
def countUsers(connection, db, table):
	cursor = connection.cursor()
	result = cursor.execute("Select count(*) from users")
	result = cursor.fetchall()
	return result[0][0]

# Retorna la media de todas las valoraciones, truncada als 2 decimals
def getAllAverage(connection, db, table):
	cursor = connection.cursor()
	cursor.execute("SELECT TRUNCATE(AVG(Valoration),2) from valorations")
	result = cursor.fetchall()
	return result[0][0]

# Retorna los datos de valoraciones por usuario
def getAveragePerUsers(connection, db, table, verbose):
	cursor = connection.cursor()
	result = cursor.execute("SELECT User_name, COUNT(*) \
		as TotalRestaurants, TRUNCATE(SUM(Valoration),2) as Valoracionstotals, AVG(Valoration) as Mitja \
		FROM SIO.valorations v GROUP BY User_name")
	if (verbose):
		print ("Getting COUNT, SUM, AVG of each user")
	result = cursor.fetchall()
	return result

# Retorna los datos de valoraciones por restaurante
def getAveragePerRest(connection, db, table, verbose):
	cursor = connection.cursor()
	result = cursor.execute("SELECT Restaurant_name, COUNT(*) \
		as TotalRestaurants, TRUNCATE(SUM(Valoration),2) as Valoracionstotals, AVG(Valoration) as Mitja \
		FROM SIO.valorations v GROUP BY Restaurant_name")
	if (verbose):
		print ("Getting COUNT, SUM, AVG of each user")
	result = cursor.fetchall()
	return result

# Retorna los datos de valoraciones por restaurante
# IMPORTANTE: Consume demasaida RAM y peta
def getAllMode(connection, db, table, verbose):
	cursor = connection.cursor()
	result = cursor.execute("SELECT Valoration FROM SIO.valorations v ")
	if (verbose):
		print ("Getting COUNT, SUM, AVG of each user")
	result = cursor.fetchall()
	df = pd.DataFrame([result])
	mode = df.mode()
	return mode

# Retorna los datos de valoraciones por restaurante
def getModePerRest(connection, db, table, rest, verbose):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE Restaurant_name = '{rest}'")
	if (verbose):
		print ("Getting mode for restaurant Restaurant1")
	result = cursor.fetchall()
	df = pd.DataFrame(tuple(result))
	mode = df.mode()
	return mode

# Retorna los datos de valoraciones por usuario
def getModePerUser(connection, db, table, user, verbose):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE User_name = '{user}'")
	if (verbose):
		print ("Getting mode for restaurant User1")
	result = cursor.fetchall()
	df = pd.DataFrame(tuple(result))
	mode = df.mode()
	return mode

# Retorna la desviacó estàndar de un usuari
def getDesvPerUser(connection, db, table, user, verbose):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE User_name = '{user}'")
	if (verbose):
		print ("Getting desv for restaurant User1")
	result = cursor.fetchall()
	df = pd.DataFrame(tuple(result))
	return (df.std(axis=0))

# Crea una gráfica scatter amb les valoracions d'un restaurant
# S'haura de revisar
def getGraphPerRest(connection, db, table, rest, verbose):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration, User_name FROM SIO.valorations v WHERE Restaurant_name = '{rest}'")
	if (verbose):
		print (f"Getting mode for restaurant {rest}")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	result_clean = []
	users = []
	for i in result:
		result_clean.append(i[0])
		users.append(i[1])

	# Crear el pandas dataframe
	df = pd.DataFrame({rest: tuple(result_clean), 
					'User': tuple(users)})

	print (df)	# Mostra les dades per pantalla
	df.plot(kind='scatter', y=rest, x='User', color='red') # Mostra la gràfica

# Retorna los datos de valoraciones por restaurante
# S'haura de revisar
def getGraphPeruser(connection, db, table, user, verbose):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration, Restaurant_name FROM SIO.valorations v WHERE User_name = '{user}'")
	if (verbose):
		print (f"Getting mode for restaurant {user}")
		# Fiquem les dades que ens interesa

	result = cursor.fetchall()
	rests = []
	valors = []
	for i in result:
		valors.append(i[0])
		rests.append(str(i[1]).replace('Restaurant', ''))
	# Crear el pandas dataframe
	df = pd.DataFrame({'Valor': tuple(valors), 
		'Rest': tuple(rests)}, 
		columns = ['Valor', 'Rest'])

	df = df.sort_values(by='Valor') # Ordenar les ades per una millor visualtzació
	print (df)  # Mostra les dades per pantalla

	df.plot.scatter(x='Rest', y='Valor')
	plt.xlabel('x - axis') 
	plt.ylabel('y - axis') 
	plt.title('My scatter plot!') 
	plt.legend() 
	plt.show()

# Muestra el histograma de valoraciones por usuario
# S'haura de revisar
def getHistoPeruser(connection, db, table, user, verbose):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration, Restaurant_name FROM SIO.valorations v WHERE User_name = '{user}'")
	if (verbose):
		print (f"Getting mode for restaurant {user}")
	result = cursor.fetchall()
	# Fiquem les dades que ens interesa
	rests = []
	valors = []
	for i in result:
		valors.append(i[0])
		rests.append(str(i[1]).replace('Restaurant', ''))
	# Crear el pandas dataframe
	df = pd.DataFrame({'Valor': tuple(valors), 
		'Rest': tuple(rests)}, 
		columns = ['Valor', 'Rest'])

	print (df) # Msotra el dataframe per pantalla
	# Crear i mostrar el gràfic
	df.plot.hist(x='Rest', y='Valor')
	plt.xlabel('RESTAUANTS')
	plt.ylabel('FREQUENCY')
	plt.show()
	

