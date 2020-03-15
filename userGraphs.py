import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import init_DB as iDB


def histrogramaUserAverage(conn):
	cursor = conn.cursor()
	result = cursor.execute(f"SELECT Mitja, User_name FROM SIO.UserData v")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	valors = []
	users = []
	for i in result:
		valors.append(i[0])
		users.append(str(i[1]).replace('User', ''))
	# Crear el pandas dataframe
	df = pd.DataFrame({'Mitja': tuple(valors),
		'Users': tuple(users)},
		columns = ['Mitja', 'Users'])

	plt.style.use('seaborn-white')
	df.hist(rwidth=0.97) # Mostra la gràfica
	plt.show()

def dispersioUserDesv(conn):
	cursor = conn.cursor()
	result = cursor.execute(f"SELECT Desv_pobl, User_name FROM SIO.UserData v")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	valors = []
	users = []
	for i in result:
		valors.append(i[0])
		users.append(str(i[1]).replace('User', ''))
	# Crear el pandas dataframe
	df = pd.DataFrame({'Desv_Std': tuple(valors),
		'Users': tuple(users)},
		columns = ['Desv_Std', 'Users'])

	plt.style.use('seaborn-white')
	df.hist(rwidth=0.97) # Mostra la gràfica
	plt.show()

def dispersioAndModeUserDesv(conn):
	cursor = conn.cursor()
	result = cursor.execute(f"SELECT Desv_pobl, Moda, User_name FROM SIO.UserData v")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	valors = []
	moda = []
	users = []
	for i in result:
		valors.append(i[0])
		moda.append(i[1])
		users.append(str(i[1]).replace('User', ''))
	# Crear el pandas dataframe
	df = pd.DataFrame({'Desv_Std': tuple(valors),
		'Moda': tuple(moda)
		'Users': tuple(users)},
		columns = ['Desv_Std', 'Moda', 'Users'])

	plt.style.use('seaborn-white')
	df.hist(rwidth=0.97) # Mostra la gràfica
	plt.show()

def possiblesUsuarisFalsos(conn):
	cursor = conn.cursor()
	result = cursor.execute(f"Select User_name \
		from UserData u where (mitja>8 or mitja <-8) \
		and (desv_pobl < 1.25 or desv_pobl > 0.75) \
		and (recompte > 60) group by User_name")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	valors = []
	for i in result:
		valors.append(i[0])
	# Crear el pandas dataframe
	df = pd.DataFrame({'Users': tuple(valors)},
		columns = ['Users'])
	print (df)

conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')
possiblesUsuarisFalsos(conn)

