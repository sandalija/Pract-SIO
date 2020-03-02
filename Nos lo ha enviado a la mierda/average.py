import pymysql
import scypi

allRestaurants = "Restaurant1, Restaurant2, Restaurant3, Restaurant4, \
    Restaurant5, Restaurant6, Restaurant7, Restaurant8, \
    Restaurant9, Restaurant10, Restaurant11, Restaurant12, \
    Restaurant13, Restaurant14, Restaurant15, Restaurant16, \
	Restaurant17, Restaurant18, Restaurant19, Restaurant20, \
    Restaurant21, Restaurant22, Restaurant23, Restaurant24, \
    Restaurant25, Restaurant26, Restaurant27, Restaurant28, \
    Restaurant29, Restaurant30, Restaurant31, Restaurant32, \
    Restaurant33, Restaurant34, Restaurant35, Restaurant36, \
    Restaurant37, Restaurant38, Restaurant39, Restaurant40, \
    Restaurant41, Restaurant42, Restaurant43, Restaurant44, \
    Restaurant45, Restaurant46, Restaurant47, Restaurant48, \
	Restaurant49, Restaurant50, Restaurant51, Restaurant52, \
    Restaurant53, Restaurant54, Restaurant55, Restaurant56, \
	Restaurant57, Restaurant58, Restaurant59, Restaurant60, \
    Restaurant61, Restaurant62, Restaurant63, Restaurant64, \
    Restaurant65, Restaurant66, Restaurant67, Restaurant68, \
    Restaurant69, Restaurant70, Restaurant71, Restaurant72, \
    Restaurant73, Restaurant74, Restaurant75, Restaurant76, \
    Restaurant77, Restaurant78, Restaurant79, Restaurant80, \
    Restaurant81, Restaurant82, Restaurant83, Restaurant84, \
    Restaurant85, Restaurant86, Restaurant87, Restaurant88, \
    Restaurant89, Restaurant90, Restaurant91, Restaurant92, \
    Restaurant93, Restaurant94, Restaurant95, Restaurant96, \
    Restaurant97, Restaurant98, Restaurant99, Restaurant100"

def __connectDB__(host, database, user, password):
	try:
		connection = pymysql.connect(host=host,
						user=user, 
						passwd=password, 
						database=database)  
		print ("\n\n Connected to " +  host + "." + database)
		# cursor = db.cursor()
		return connection 
	except Exception as e:
		print ("Connection failed")
		print(e)
		raise

conn = __connectDB__('localhost', 'SIO', 'user', 'user')

mycursor = conn.cursor()

mycursor.execute("SELECT " + allRestaurants + " FROM SIO.dataset LIMIT 10")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)