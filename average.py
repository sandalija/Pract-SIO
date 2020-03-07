import pymysql
import pandas as pd
import matplotlib.pyplot as plt


# Retorna la cantidad de valoraciones
def countUsers(connection, db, table):
	cursor = connection.cursor()
	result = cursor.execute("Select count(*) from users")
	result = cursor.fetchall()
	return result[0][0]

# Retorna la media de todas las valoraciones
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
# Consume demasaida RAM y peta
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
	#df = pd.DataFrame([result])
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
	#df = pd.DataFrame([result])
	mode = df.mode()
	return mode

def getDesvPerUser(connection, db, table, user, verbose):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration FROM SIO.valorations v WHERE User_name = '{user}'")
	if (verbose):
		print ("Getting desv for restaurant User1")
	result = cursor.fetchall()
	df = pd.DataFrame(tuple(result))
	return (df.std(axis=0))

# Retorna los datos de valoraciones por restaurante
def getGraphPerRest(connection, db, table, rest, verbose):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration, User_name FROM SIO.valorations v WHERE Restaurant_name = '{rest}'")
	if (verbose):
		print (f"Getting mode for restaurant {rest}")
	result = cursor.fetchall()
	result_clean = []
	users = []
	for i in result:
		result_clean.append(i[0])
		users.append(i[1])
	df = pd.DataFrame({rest: tuple(result_clean), 
					'User': tuple(users)})
	print (df)
	# print (df)
	df.plot(kind='scatter', y=rest, x='User', color='red')

# Retorna los datos de valoraciones por restaurante
def getGraphPeruser(connection, db, table, rest, verbose):
	cursor = connection.cursor()
	result = cursor.execute(f"SELECT Valoration, Restaurant_name FROM SIO.valorations v WHERE User_name = '{rest}'")
	if (verbose):
		print (f"Getting mode for restaurant {rest}")
	result = cursor.fetchall()
	result_clean = []
	users = []
	for i in result:
		result_clean.append(i[0])
		users.append(i[1])
	df = pd.DataFrame({rest: tuple(result_clean), 
					'Rest': tuple(users)})
	print (df)
	# print (df)
	df.plot(kind='scatter', y=rest, x='User', color='red')