import pymysql


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
cursor.execute("SELECT * FROM SIO.valorations")
result= cursor.fetchall()
#es pot fer també bucle fetchone()
users=""
for i in result:
    users=users+""+str(result)
print ('end')
