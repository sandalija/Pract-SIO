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
	plt.title('Histograma de la mitja de cada usuari')
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
	plt.title('Dispersió de la desviació estándar per cada usuari')
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
	df = pd.DataFrame({'Desviació estàndar per usuari': tuple(valors),
		'Moda per usuari': tuple(moda),
		'Users': tuple(users)},
		columns = ['Desviació estàndar per usuari', 'Moda per usuari', 'Users'])

	plt.style.use('seaborn-white')
	df.hist(rwidth=0.97) # Mostra la gràfica
	plt.show()

def possiblesUsuarisFalsos(conn):
	cursor = conn.cursor()
	result = cursor.execute(f"Select User_name, Mitja, Recompte, Desv_pobl, Mediana \
		from UserData u where (mitja>8 or mitja <-8) \
		and (desv_pobl < 1.25 or desv_pobl > 0.75) \
		and (recompte > 60) group by User_name")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	users = []
	mitja = []
	recompte = []
	desv = []
	mediana = []
	for i in result:
		users.append(i[0])
		mitja.append(i[1])
		recompte.append(i[2])
		desv.append(i[3])
		mediana.append(i[4])
	# Crear el pandas dataframe
	df = pd.DataFrame({'Users': tuple(users),
			'Mitja': tuple(mitja),
			'Recompte': tuple(recompte),
			'Desv': tuple(recompte),
			'Mediana': tuple(mediana)},
		columns = ['Users', 'Mitja', 'Recompte', 'Desv', 'Mediana'])
	"""print ("Usuari\tMitja\tRecompte\tDesv\tMediana")
	for index, row in df.iterrows():
		print(str(row['Users']) +"\t"+ str(row['Mitja']) +"\t"+ str(row['Recompte']) \
			 +"\t"+ str(row['Desv']) +"\t"+ str(row['Mediana']))"""
	aux = []
	for index, row in df.iterrows():
		aux.append(row['Users'])
	print (aux)
	print ("Son un total de " + str(len(aux)))

conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')
histrogramaUserAverage(conn)
dispersioUserDesv(conn)
dispersioAndModeUserDesv(conn)
possiblesUsuarisFalsos(conn)

