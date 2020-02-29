# Primeros pasos

1. Crear una BD MySQL en localhost:3306 con el usuario 'user' y la contraseña 'user'

````bash
$ sudo apt install mysql-server
$ sudo mysql
````

> Si sale ``ERROR 2002: ...`` Ver [solución](https://www.digitalocean.com/community/questions/mysql-can-t-connect-to-local-mysql-server-through-socket-var-run-mysqld-mysqld-sock-2)


````mySQL
CREATE USER 'user'@'localhost' IDENTIFIED BY 'user';
GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
CREATE DATABASE SIO;
````

A partir de aquí, debes de poder iniciar sesión como ``user`` desde una terminal. La conexión también funciona desde MySQL Workbench

2. Instalar el connector de Python con Mysql ``pymysql``