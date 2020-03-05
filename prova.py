import pymysql
import pandas as pd

def __connectDB__(host, database, user, password):
	try:
		connection = pymysql.connect(host=host,
						user=user,
						passwd=password,
						database=database)
		print ("\n\nConnected to " +  host + "." + database)
		# cursor = db.cursor()
		return connection
	except Exception as e:
		print ("Connection failed")
		print(e)
		raise


conn = __connectDB__('localhost', 'SIO', 'user', 'user')

cursor = conn.cursor()
#SELECT AVG(Valoration) from valorations v

data= cursor.execute("SELECT User_name, COUNT(*) as TotalRestaurants, SUM(Valoration) as Valoracionstotals, AVG(Valoration) as Mitja FROM SIO.valorations v GROUP BY User_name")
#data= cursor.fetchone()
#print (f"printo cursor:  {data}")
result= cursor.fetchall()
#print(result)

#SELECT User_name, COUNT(*), SUM(Valoration) FROM SIO.valorations v GROUP BY User_name



#es pot fer també bucle fetchone()
users=""
for i in result:
    print(i[0],i[1],i[2])
#print (f'{users}')
