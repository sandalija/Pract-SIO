
import csv
import pymysql
import os
from os.path import expanduser



DATASET = 'dataset.csv'


def getDatasetDir():
	if os.name == 'nt':
		return (expanduser("~") + str("\\") + DATASET)
	else:
		return (expanduser("~") + str("/") + DATASET)

def __connectDB__(host, database, user, password):
	try:
		db = pymysql.connect(host=host,
						user=user, 
						passwd=password, 
						database=database)  
		print ("\n\n Connected to " +  host + "." + database)
		cursor = db.cursor()
		return cursor 
	except Exception as e:
		print ("Connection failed")
		print(e)
		raise
	
home = getDatasetDir()
print (home)

cursor = __connectDB__('localhost', 'SIO', 'user', 'user')


