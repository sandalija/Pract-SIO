import pymysql
import csv

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

def loadCSV(dataFile, connection, db, table):
	csv_data = csv.reader(open(dataFile))
	cursor = connection.cursor()

	for row in csv_data:
		splitedRow = row[0].split(';')
		# print(splitedRow)
		user = splitedRow[0]

		#crear user
		cursor.execute("SELECT COUNT(*) FROM users WHERE User_name = %s", (user))
		# gets the number of rows affected by the command executed
		row_count = cursor.rowcount
		if row_count == 0:
			cursor.execute("INSERT INTO users (User_name) VALUES (%s)", (user))

		for i in range (1, len(splitedRow)):
			if (float(splitedRow[i]) >= (-10) and float(splitedRow[i]) <= 10):
				restaurant = "Restaurant"+str(i)
				# print (f"User: {user} Rest: {restaurant} Value: {splitedRow[i]}")

				# mycursor.execute("INSERT INTO)
	myresult = cursor.fetchall()


conn = __connectDB__('localhost', 'SIO', 'user', 'user')
loadCSV('C:\Pract-SIO/Pract-SIO/dataset.csv', conn, 'SIO', 'valorations')
print ("end")

