import pymysql
import csv

allRestaurants = ['Restaurant1', ' Restaurant2', ' Restaurant3', ' Restaurant4', ' \
    Restaurant5', ' Restaurant6', ' Restaurant7', ' Restaurant8', ' \
    Restaurant9', ' Restaurant10', ' Restaurant11', ' Restaurant12', ' \
    Restaurant13', ' Restaurant14', ' Restaurant15', ' Restaurant16', ' \
	Restaurant17', ' Restaurant18', ' Restaurant19', ' Restaurant20', ' \
    Restaurant21', ' Restaurant22', ' Restaurant23', ' Restaurant24', ' \
    Restaurant25', ' Restaurant26', ' Restaurant27', ' Restaurant28', ' \
    Restaurant29', ' Restaurant30', ' Restaurant31', ' Restaurant32', ' \
    Restaurant33', ' Restaurant34', ' Restaurant35', ' Restaurant36', ' \
    Restaurant37', ' Restaurant38', ' Restaurant39', ' Restaurant40', ' \
    Restaurant41', ' Restaurant42', ' Restaurant43', ' Restaurant44', ' \
    Restaurant45', ' Restaurant46', ' Restaurant47', ' Restaurant48', ' \
	Restaurant49', ' Restaurant50', ' Restaurant51', ' Restaurant52', ' \
    Restaurant53', ' Restaurant54', ' Restaurant55', ' Restaurant56', ' \
	Restaurant57', ' Restaurant58', ' Restaurant59', ' Restaurant60', ' \
    Restaurant61', ' Restaurant62', ' Restaurant63', ' Restaurant64', ' \
    Restaurant65', ' Restaurant66', ' Restaurant67', ' Restaurant68', ' \
    Restaurant69', ' Restaurant70', ' Restaurant71', ' Restaurant72', ' \
    Restaurant73', ' Restaurant74', ' Restaurant75', ' Restaurant76', ' \
    Restaurant77', ' Restaurant78', ' Restaurant79', ' Restaurant80', ' \
    Restaurant81', ' Restaurant82', ' Restaurant83', ' Restaurant84', ' \
    Restaurant85', ' Restaurant86', ' Restaurant87', ' Restaurant88', ' \
    Restaurant89', ' Restaurant90', ' Restaurant91', ' Restaurant92', ' \
    Restaurant93', ' Restaurant94', ' Restaurant95', ' Restaurant96', ' \
    Restaurant97', ' Restaurant98', ' Restaurant99', ' Restaurant100']

allUsers = []



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

	allRest = next(csv_data)
	allRest = allRest[0].split(';')
	# print(allRest)
	for rest in allRest[1:]:
		# print ("INSERT INTO restaurtants (restaurants_name) VALUES (%s)", (rest))
		cursor.execute("INSERT INTO " + db + ".restaurants (Restaurant_name) VALUES (%s)", (rest))
	connection.commit()

	for row in csv_data:
		splitedRow = row[0].split(';')
		# print(splitedRow)
		user = splitedRow[0]

		#crear user
		# print("SELECT COUNT(*) FROM users WHERE User_name = %s", (user))
		cursor.execute("SELECT COUNT(*) FROM " + db + ".users WHERE User_name = %s", (user))
		# gets the number of rows affected by the command executed
		result=cursor.fetchone()
		row_count = result[0]
		# ("row count = " + str(row_count))
		if row_count == 0:
			#print ("INSERT INTO users (User_name) VALUES (%s)", (user))
			cursor.execute("INSERT INTO " + db + ".users (User_name) VALUES (%s)", (user))

		connection.commit()
		for i in range (1, len(splitedRow)):
			if (float(splitedRow[i]) != 99):
				restaurant = "Restaurant"+str(i)
				#print (f"User: {user} Rest: {restaurant} Value: {splitedRow[i]}")
				cursor.execute("INSERT INTO " + db + ".valorations (User_name, Restaurant_name, Valoration) \
					VALUES (%s, %s, %s)", (user, restaurant, str(splitedRow[i])))

	connection.commit()

# Retorna la media de todas las valoraciones
def getAllAverage(connection, db, table):
	cursor = connection.cursor()
	cursor.execute("SELECT TRUNCATE(AVG(Valoration),2) from valorations")
	result = cursor.fetchall()
	return result[0][0]

# Retorna la cantidad de valoraciones
def countUsers(connection, db, table):
	cursor = connection.cursor()
	result = cursor.execute("Select count(*) from users")
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
def getAllMode(connection, db, table, verbose):
	cursor = connection.cursor()
	result = cursor.execute("SELECT Valoration, COUNT(*) \
		as TotalRestaurants, TRUNCATE(SUM(Valoration),2) as Valoracionstotals, AVG(Valoration) as Mitja \
		FROM SIO.valorations v GROUP BY Restaurant_name")
	if (verbose):
		print ("Getting COUNT, SUM, AVG of each user")
	result = cursor.fetchall()
	return result


conn = __connectDB__('localhost', 'SIO', 'user', 'user')
#loadCSV('/home/sergio/Pract-SIO/dataset.csv', conn, 'SIO', 'valorations')

# Number of users and list with them
n_users = countUsers(conn, 'SIO', 'users')
print ("# users " + str(n_users))
for n in range(0, n_users):
	allUsers.append("Users"+str(n))

# Average of all users
average = getAllAverage(conn, 'SIO', 'valorations')
print ("AVERAGE: " + str(average))

# Average per user
averageUser =  getAveragePerUsers(conn, 'SIO', 'users', True)
print ("Averange per user")
print(averageUser)

# Average per rest
averageRest =  getAveragePerRest(conn, 'SIO', 'users', True)
print ("Averange per user")
print(averageUser)



print ("end")
