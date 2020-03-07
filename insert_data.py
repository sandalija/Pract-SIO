import pymysql
import csv
import pandas as pd

import init_DB as iDB
import average as aver
import graph as gp
import matplotlib

conn = iDB.__connectDB__('localhost', 'SIO', 'user', 'user')
#loadCSV('/home/sergio/Pract-SIO/dataset.csv', conn, 'SIO', 'valorations')

iDB.__getUsersName__(conn, 'SIO', 'valorations')

modo = int(input('Enter your input:'))
print ("Modo " + str(modo))

if (modo == 1):
    aver.getGraphPeruser(conn, 'SIO', 'users', 'User1', True)
else:

    # Average of all users
    average = aver.getAllAverage(conn, 'SIO', 'valorations')
    print ("\nAVERAGE OK: " + str(average))

    # Number of users
    n_users = aver.countUsers(conn, 'SIO', 'valorations')
    print ("\n# USERS OK: " + str(n_users))

    # Average per user
    averageUser =  aver.getAveragePerUsers(conn, 'SIO', 'users', True)
    print ("\nAverange per user: OK")
    # print(averageUser)

    # Average per rest
    averageRest =  aver.getAveragePerRest(conn, 'SIO', 'users', True)
    print ("\nAverange per user: OK")
    #print(averageUser)

    # Mode in general
    """
    # PETARÁ
    modeAll = aver.getAllMode(conn, 'SIO', 'users', True)
    print ("\nMode: " + str(modeAll))
    """

    # Mode per user
    modeRest = aver.getModePerUser(conn, 'SIO', 'users', 'User1', True)
    print ("\nMode: " + str(modeRest))


print ("end")
