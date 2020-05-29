import pymysql as sql
import csv
import init_DB as iDB


sourceFile = './PlantillaPrediccions.csv'
conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')
dbTable = 'SIO.valorations'
token = 'prediccions'


def calcularValor(usuari, restaurant):
    cursor =conn.cursor()
    cursor.execute(f"SELECT AvgValorations from SIO.users where User_name='{usuari}'")
    mitjanaUsuari=cursor.fetchall()
    # print(f"mitjana= {mitjanaUsuari[0][0]}")
    cursor.execute(f"SELECT User_name, AvgValorations from SIO.users where AvgValorations >= '{mitjanaUsuari[0][0]}'-0.25 and AvgValorations<='{mitjanaUsuari[0][0]}'+0.25")
    usuaris_propers=cursor.fetchall()
    total=0
    total_usuaris=len(usuaris_propers)
    print(f"Usuari: {usuari}, restaurant: {restaurant}")
    #print(f"llargada= {total_usuaris}")
    for usuari_restaurant in usuaris_propers:
        #print(f"usuari restaurant={usuari_restaurant}")
        cursor.execute(f"Select Valoration from SIO.valorations where User_name='{usuari_restaurant[0]}' and Restaurant_name='{restaurant}'")
        valor=cursor.fetchall()
        try:
            total+=valor[0][0]
        except IndexError:
            # print("No hi ha res")
            total_usuaris -= 1
       #print(f"el total=:{total}")
    return total/total_usuaris
    

# Genera el csv para subirlo a la web 
# Peterá si las casillas están vacías
def generateCSV(sourceFile, conn, dbTable, token):
    predictions = open(token, "w+")
    cursor = conn.cursor()
    ## Leer el CSV del profe
    with open(sourceFile) as source:
        csv_reader = csv.reader(source, delimiter=';')
        line_count = 0
        #resultat=[]
        for row in csv_reader:
            ## Por cada fila del csv fuente
            """  row[0] = 'User1'
            row[1] = 'Restaurant1' """
            resultat=calcularValor(row[0],row[1])
            #cursor.execute(f"SELECT Valoration FROM {dbTable} WHERE User_name = '{row[0]}' AND Restaurant_name = '{row[1]}'")
            #val = cursor.fetchall()
            # print(f'{row[0]};{row[1]};{val[0][0]} ')
            print(f'{row[0]};{row[1]};{resultat} ')
            puntuacio=round(resultat,4)
            predictions.write(f'{row[0]};{row[1]};{puntuacio}\n')
            line_count += 1
        # print(f'Processed {line_count} lines.')
    predictions.close()



generateCSV(sourceFile, conn, dbTable, token)
