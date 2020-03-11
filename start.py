import pymysql
import csv
import pandas as pd

import init_DB as iDB
import functions as func
import graph as gp
import matplotlib

## Fitxer princiapl (main)

# Ens connectem a la BD SIO com 'user'
conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')

# Insertar en la DB.
# Descomentar per insertar
#loadCSV('/home/sergio/Pract-SIO/dataset.csv', conn, 'SIO', 'valorations')

# Inicializamos el número de usuariis (iDB.allUser)
iDB.__getUsersName__(conn, 'SIO', 'valorations')

# Vaig ficar això de manera que podem anar testejant la funció si mode == 1
# Si no és 1, hauria de executrar-se lo que sería el main final.
modo = int(input('Enter your input:'))
print ("Modo " + str(modo))
if (modo == 1):
    iDB.loadCSV('C:\Pract-SIO/Pract-SIO/dataset.csv', conn, 'SIO', 'users')
    func.getGraphPeruser(conn, 'SIO', 'users', 'User1', True)
else:
    # funcage of all users
    funcage = func.getAllfuncage(conn, 'SIO', 'valorations')
    print ("\nfuncAGE OK: " + str(funcage))

    # Number of users
    n_users = func.countUsers(conn, 'SIO', 'valorations')
    print ("\n# USERS OK: " + str(n_users))

    # funcage per user
    funcageUser =  func.getfuncagePerUsers(conn, 'SIO', 'users', True)
    print ("\nfuncange per user: OK")
    # print(funcageUser)

    # funcage per rest
    funcageRest =  func.getfuncagePerRest(conn, 'SIO', 'users', True)
    print ("\nfuncange per user: OK")
    #print(funcageUser)

    # Mode in general
    """
    # PETARÁ
    modeAll = func.getAllMode(conn, 'SIO', 'users', True)
    print ("\nMode: " + str(modeAll))
    """

    # Mode per user
    modeRest = func.getModePerUser(conn, 'SIO', 'users', 'User1', True)
    print ("\nMode: " + str(modeRest))


print ("end")
