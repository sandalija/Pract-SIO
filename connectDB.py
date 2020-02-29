
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

home = getDir()
print (home)

try:
    db = pymysql.connect(host='localhost',
                        user='user', 
                        passwd='user', 
                        database='SIO')
except Exception as e:
    print ("Connection failed")
    print(e)
    raise

print ("\n\n Connected to ")


cursor = db.cursor()

csv_data = csv.reader(open('/home/sergio/SIO/dataset.csv'))
for row in csv_data:

    cursor.execute("INSERT INTO root.sio(user, Restaurant1, \
    Restaurant2, \
    Restaurant3, \
    Restaurant4, \
    Restaurant5, \
    Restaurant6, \
    Restaurant7, \
    Restaurant8, \
    Restaurant9, \
    Restaurant10, \
    Restaurant11, \
    Restaurant12, \
    Restaurant13, \
    Restaurant14, \
    Restaurant15, \
    Restaurant16, \
    Restaurant17, \
    Restaurant18, \
    Restaurant19, \
    Restaurant20, \
    Restaurant21, \
    Restaurant22, \
    Restaurant23, \
    Restaurant24, \
    Restaurant25, \
    Restaurant26, \
    Restaurant27, \
    Restaurant28, \
    Restaurant29, \
    Restaurant30, \
    Restaurant31, \
    Restaurant32, \
    Restaurant33, \
    Restaurant34, \
    Restaurant35, \
    Restaurant36, \
    Restaurant37, \
    Restaurant38, \
    Restaurant39, \
    Restaurant40, \
    Restaurant41, \
    Restaurant42, \
    Restaurant43, \
    Restaurant44, \
    Restaurant45, \
    Restaurant46, \
    Restaurant47, \
    Restaurant48, \
    Restaurant49, \
    Restaurant50, \
    Restaurant51, \
    Restaurant52, \
    Restaurant53, \
    Restaurant54, \
    Restaurant55, \
    Restaurant56, \
    Restaurant57, \
    Restaurant58, \
    Restaurant59, \
    Restaurant60, \
    Restaurant61, \
    Restaurant62, \
    Restaurant63, \
    Restaurant64, \
    Restaurant65, \
    Restaurant66, \
    Restaurant67, \
    Restaurant68, \
    Restaurant69, \
    Restaurant70, \
    Restaurant71, \
    Restaurant72, \
    Restaurant73, \
    Restaurant74, \
    Restaurant75, \
    Restaurant76, \
    Restaurant77, \
    Restaurant78, \
    Restaurant79, \
    Restaurant80, \
    Restaurant81, \
    Restaurant82, \
    Restaurant83, \
    Restaurant84, \
    Restaurant85, \
    Restaurant86, \
    Restaurant87, \
    Restaurant88, \
    Restaurant89, \
    Restaurant90, \
    Restaurant91, \
    Restaurant92, \
    Restaurant93, \
    Restaurant94, \
    Restaurant95, \
    Restaurant96, \
    Restaurant97, \
    Restaurant98, \
    Restaurant99, \
    Restaurant100)  \
     VALUES ('%s', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', \
            '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', \
            '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', \
            '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', \
            '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', \
            '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', \
            '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', \
            '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', \
            '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', \
            '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i')", 
          row)
#close the connection to the database.
db.commit()
cursor.close()


print ("Done")