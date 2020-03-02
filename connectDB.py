
import csv
import pymysql
import os
from os.path import expanduser



DATASET = 'dataset.csv'
DATASET_CLEAN = 'dataset_clean.csv'


def getDatasetDir():
	if os.name == 'nt':
		return (expanduser("~") + str("\\") + DATASET)
	else:
		return (expanduser("~") + str("/") + DATASET)

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

def createTableSample(connection, database, table):
	connection.cursor().execute("CREATE TABLE customers IF NOT EXISTS (name VARCHAR(255), address VARCHAR(255))")


def createTableSIO(connection, db, table):
	connection.cursor().execute('create table if not exists '+db+'.'+table +'(User varchar(50), \
    Restaurant1 FLOAT, Restaurant2 FLOAT, Restaurant3 FLOAT, Restaurant4 FLOAT, \
    Restaurant5 FLOAT, Restaurant6 FLOAT, Restaurant7 FLOAT, Restaurant8 FLOAT, \
    Restaurant9 FLOAT, Restaurant10 FLOAT, Restaurant11 FLOAT, Restaurant12 FLOAT, \
    Restaurant13 FLOAT, Restaurant14 FLOAT, Restaurant15 FLOAT, Restaurant16 FLOAT, \
	Restaurant17 FLOAT, Restaurant18 FLOAT, Restaurant19 FLOAT, Restaurant20 FLOAT, \
    Restaurant21 FLOAT, Restaurant22 FLOAT, Restaurant23 FLOAT, Restaurant24 FLOAT, \
    Restaurant25 FLOAT, Restaurant26 FLOAT, Restaurant27 FLOAT, Restaurant28 FLOAT, \
    Restaurant29 FLOAT, Restaurant30 FLOAT, Restaurant31 FLOAT, Restaurant32 FLOAT, \
    Restaurant33 FLOAT, Restaurant34 FLOAT, Restaurant35 FLOAT, Restaurant36 FLOAT, \
    Restaurant37 FLOAT, Restaurant38 FLOAT, Restaurant39 FLOAT, Restaurant40 FLOAT, \
    Restaurant41 FLOAT, Restaurant42 FLOAT, Restaurant43 FLOAT, Restaurant44 FLOAT, \
    Restaurant45 FLOAT, Restaurant46 FLOAT, Restaurant47 FLOAT, Restaurant48 FLOAT, \
	Restaurant49 FLOAT, Restaurant50 FLOAT, Restaurant51 FLOAT, Restaurant52 FLOAT, \
    Restaurant53 FLOAT, Restaurant54 FLOAT, Restaurant55 FLOAT, Restaurant56 FLOAT, \
	Restaurant57 FLOAT, Restaurant58 FLOAT, Restaurant59 FLOAT, Restaurant60 FLOAT, \
    Restaurant61 FLOAT, Restaurant62 FLOAT, Restaurant63 FLOAT, Restaurant64 FLOAT, \
    Restaurant65 FLOAT, Restaurant66 FLOAT, Restaurant67 FLOAT, Restaurant68 FLOAT, \
    Restaurant69 FLOAT, Restaurant70 FLOAT, Restaurant71 FLOAT, Restaurant72 FLOAT, \
    Restaurant73 FLOAT, Restaurant74 FLOAT, Restaurant75 FLOAT, Restaurant76 FLOAT, \
    Restaurant77 FLOAT, Restaurant78 FLOAT, Restaurant79 FLOAT, Restaurant80 FLOAT, \
    Restaurant81 FLOAT, Restaurant82 FLOAT, Restaurant83 FLOAT, Restaurant84 FLOAT, \
    Restaurant85 FLOAT, Restaurant86 FLOAT, Restaurant87 FLOAT, Restaurant88 FLOAT, \
    Restaurant89 FLOAT, Restaurant90 FLOAT, Restaurant91 FLOAT, Restaurant92 FLOAT, \
    Restaurant93 FLOAT, Restaurant94 FLOAT, Restaurant95 FLOAT, Restaurant96 FLOAT, \
    Restaurant97 FLOAT, Restaurant98 FLOAT, Restaurant99 FLOAT, Restaurant100 FLOAT, \
    PRIMARY KEY (User) \
) ENGINE InnoDB; ')


def cleanCSV(datafile, datafile_clean):
	f = open(datafile, 'r')
	data = csv.reader(f, delimiter =';')
	w = open(datafile_clean, 'w')
	specials = '99'
	result = []

	for line in data:
		line = [value.replace(specials, '') for value in line]
		line = [value.replace(specials, '\'') for value in line]
		w.write("%s\n" % line)
		result.append(line)
	f.close()
	w.close()

def loadCSV(dataFile, connection, db, table):
	cursor = connection.cursor()

	csv_data = csv.reader(open(dataFile))
	#cursor.execute("LOAD DATA INFILE 'dataset_clean.csv' INTO TABLE SIO.dataset ")

	for row in csv_data:
		splitedRow = row[0].split(';')
		# print(splitedRow)
		cursor.execute("INSERT INTO SIO.dataset VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", splitedRow)
	#close the connection to the database.
	connection.commit()
	cursor.close()
		#print(splitedRow)

	
home = getDatasetDir()
print (home)

print("\n1.\n")
conn = __connectDB__('localhost', 'SIO', 'user', 'user')
print("\n2.\n")
createTableSIO(conn, 'SIO', 'dataset')
print("\n3.\n")
loadCSV(getDatasetDir(), conn, 'SIO', 'dataset')


