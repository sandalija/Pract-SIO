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


conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')
percentils(conn)
