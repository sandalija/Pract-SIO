import pymysql as pysql


# mysql-connector-python 8.0.19

db = pysql.connect(host="localhost",
                    user="root",
                    password = "root"
                    db="SIO")