import csv
import pymysql
import os
from os.path import expanduser

DATASET = 'dataset.csv'


def getDir():
    if os.name == 'nt':
        return (expanduser("~") + str("\\") + DATASET)
    else:
        return (expanduser("~") + str("/") + DATASET)

home = getDir()
print (home)