USE SIO;
DROP TABLE UserData;
DROP TABLE RestaurantData;

CREATE TABLE IF NOT EXISTS UserData
(
    User_name varchar(50),
    Mitja float,
    Mediana float,
    Recompte int,
    Desv_pobl float,
    Moda int,
    Primary key(User_name)
) Engine = InnoDB;

CREATE TABLE IF NOT EXISTS RestaurantData
(
    Restaurant_name varchar(50),
    Mitja float,
    Mediana float,
    Recompte int,
    Desv_pobl float,
    Moda int,
    Primary key(Restaurant_name)
) Engine = InnoDB;