import pymysql as sql
import csv
import init_DB as iDB


sourceFile = './PlantillaPrediccions.csv'
conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')
dbTable = 'SIO.valorations'
token = 'prediccions'

# Genera el csv para subirlo a la web 
# Peterá si las casillas están vacías
def generateCSV(sourceFile, conn, dbTable, token):
    predictions = open(token, "w+")
    cursor = conn.cursor()
    ## Leer el CSV del profe
    with open(sourceFile) as source:
        csv_reader = csv.reader(source, delimiter=';')
        line_count = 0
        for row in csv_reader:
            ## Por cada fila del csv fuente
            """  row[0] = 'User1'
            row[1] = 'Restaurant1' """
            cursor.execute(f"SELECT Valoration FROM {dbTable} WHERE User_name = '{row[0]}' AND Restaurant_name = '{row[1]}'")
            val = cursor.fetchall()
            # print(f'{row[0]};{row[1]};{val[0][0]} ')
            predictions.write(f'{row[0]};{row[1]};{val[0][0]}\n')
            line_count += 1
        print(f'Processed {line_count} lines.')
    predictions.close()

generateCSV(sourceFile, conn, dbTable, token)
