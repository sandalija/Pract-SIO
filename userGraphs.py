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
	df.plot.kde()
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

# Peta
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
		from UserData u where (mitja > 8 or mitja < -8) \
		and (desv_pobl < -2.9 or desv_pobl > 3.93) \
		group by User_name")
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

def dispersioUserMitja(conn):
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
	df.plot(kind='scatter', x='Users', y='Mitja') # Mostra la gràfica
	plt.title('Mitja per cada usuari')
	plt.show()

def densitivyRestUser(conn, user):
	cursor = conn.cursor()
	result = cursor.execute(f"SELECT Valoration, User_name FROM SIO.valorations v WHERE User_name = '{user}';")
	result = cursor.fetchall()

	# Fiquem les dades que ens interesa
	valors = []
	rests = []
	for i in result:
		valors.append(i[0])
		rests.append(str(i[1]).replace('User', ''))
	# Crear el pandas dataframe
	df = pd.DataFrame({'Mitja': tuple(valors),
		'User': tuple(rests)},
		columns = ['Mitja', 'User'])
	print (df)
	df.plot(kind='density')
	df.hist(rwidth=0.97)
	plt.show()

def percentilsDesvUser(connection):
	cursor = connection.cursor()
	result = cursor.execute("Select Desv_pobl from SIO.UserData")
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
	plt.title("Diagrama de caixes de la dispersió de les desviacions dels usuari")
	plt.show()
	df.hist(rwidth=0.97)
	plt.style.use('seaborn-white')
	plt.title("Histograma de la dispersió de les desviacions dels usuaris")
	plt.show()

def percentilsAverageUser(connection):
	cursor = connection.cursor()
	result = cursor.execute("Select Mitja from SIO.UserData")
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
	plt.title("Diagrama de la dispersió de les mitjes dels usuaris")
	plt.show()
	df.hist(rwidth=0.97)
	plt.style.use('seaborn-white')
	plt.title("Histograma de la dispersió de les mitjes dels usuaris")
	plt.show()

conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')
histrogramaUserAverage(conn)
dispersioUserDesv(conn)
dispersioAndModeUserDesv(conn)
percentilsDesvUser(conn)
percentilsAverageUser(conn)
possiblesUsuarisFalsos(conn)
densitivyRestUser(conn, 'User1')
densitivyRestUser(conn, 'User2')
densitivyRestUser(conn, 'User3')
densitivyRestUser(conn, 'User4')
densitivyRestUser(conn, 'User5')


