CREATE DATABASE IF NOT EXISTS SIO;

USE SIO;

DELETE FROM users;
DELETE FROM restaurants;
DELETE FROM valorations;

CREATE TABLE IF NOT EXISTS users
(
    User_name varchar(50),
    Primary key(User_name)
) Engine = InnoDB;

CREATE TABLE IF NOT EXISTS restaurants
(
    Restaurant_name varchar(50),
    Primary key(Restaurant_name)
) Engine = InnoDB;

CREATE TABLE IF NOT EXISTS valorations
(
    User_name int NOT NULL,
    Restaurant_name int NOT NULL,
    Valoration float NOT NULL,
    FOREIGN KEY (User_name) REFERENCES users (User_name),
    FOREIGN KEY (Restaurant_name) REFERENCES restaurants (Restaurant_name),
    Primary key(Restaurant_name, User_name)
) Engine = InnoDB;