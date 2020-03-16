import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import init_DB as iDB


def percentils(connection):
	cursor = connection.cursor()
	result = cursor.execute("Select Valoration from SIO.valorations")
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
	ply.title("Diagrama de caixes de totes les valoracions")
	plt.show()
	df.hist(rwidth=0.97)
	plt.style.use('seaborn-white')
	ply.title("Histograma de totes les valoracions")
	plt.show()

def percentilsRecompte(connection):
	cursor = connection.cursor()
	result = cursor.execute("Select Recompte from SIO.UserData")
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
	plt.title("Diagrama de caixes del recompte de valoracions per usuari")
	plt.show()
	df.hist(rwidth=0.97)
	plt.style.use('seaborn-white')
	plt.title("Histograma del recompte de valoracions per usuari")
	plt.show()

def percentilsRecompte2(connection):
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
	plt.title("Diagrama de caixes de les mitjes de valoracions per restaurant")
	plt.show()
	df.hist(rwidth=0.97)
	plt.style.use('seaborn-white')
	plt.title("Histograma de les mitjes de valoracions per restaurant")
	plt.show()

def percentilsRecompte2(connection):
	cursor = connection.cursor()
	result = cursor.execute("Select Mitja from SIO.UserData")
	result = cursor.fetchall()
	result_clean = []
	users = []
	for i in result:
		result_clean.append(i[0])
	df = pd.DataFrame({'Valor': tuple(result_clean)}, columns=['Valor'])
	print ("Mediana " + str(df['Valor'].quantile(0.50)))
	print ("mitja" + str(df.mean()))
	print ("Desv"  + str(df.std()))
	print ("Moda " +str(df.mode()))

conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')
percentilsRecompte2(conn)
