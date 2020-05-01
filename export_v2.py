import pymysql as sql
import csv
import init_DB as iDB
import threading



sourceFile = './prediccions.csv'
dbTable = 'SIO.valorations'
token = 'prediccions'


def auxCalcValor(position, index):
    predictions = open(token+"_"+str(index), "w+")
    print ("In aux function")
    s = []
    for p in position:
        print(f'{p[0]};{p[1]}')
        s.append([p[0], p[1], calcularValor(p[0], p[1])])
    for r in s:
      predictions.write(f'{r[0]};{r[1]};{r[2]}\n')


def calcularValor(usuari, restaurant):
    conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')
    print (f"USUARIO {usuari}, RESTAURANTE {restaurant}")
    cursor =conn.cursor()
    cursor.execute(f"SELECT AvgValorations from SIO.users where User_name='{usuari}'")
    mitjanaUsuari=cursor.fetchall()
    # print(f"mitjana= {mitjanaUsuari[0][0]}")
    cursor.execute(f"SELECT User_name from SIO.users where AvgValorations >= '{mitjanaUsuari[0][0]}'-1 and AvgValorations<='{mitjanaUsuari[0][0]}'+1")
    usuaris_propers=cursor.fetchall()
    total=0
    total_usuaris=len(usuaris_propers)
    #print(f"Usuari: {usuari}, restaurant: {restaurant}")
    #print(f"llargada= {total_usuaris}")
    for usuari_restaurant in usuaris_propers:
        # print(f"usuari restaurant={usuari_restaurant}")
        cursor.execute(f"Select Valoration from SIO.valorations where User_name='{usuari_restaurant[0]}' and Restaurant_name='{restaurant}'")
        valor=cursor.fetchall()
        try:
            total+=valor[0][0]
        except IndexError:
            # print("No hi ha res")
            total_usuaris -= 1
       # print(f"el total=:{total}")
    conn.close()
    return total/total_usuaris

n = int(input("Num de threads: "))
positions = []
for m in range (0, n):
    positions.append([])
rows = []
predictions = open(token, "w+")
with open(sourceFile) as source:
    csv_reader = csv.reader(source, delimiter=';')
    line_count = 0
    for row in csv_reader:
        rows.append([row[0], row[1]])
        line_count += 1
predictions.close()

for i in range(0, line_count):
    print (str(int(i %n)))
    positions[int(i % n)].append(rows[i])

print (positions)

threats = []
i=1
for p in positions:
    t = threading.Thread(target=auxCalcValor, args=(p, i))
    t.start()
    threats.append(t)
    i+= 1

for t in threats:
    t.join()
print ("FIN")





