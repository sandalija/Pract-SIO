# Pràctica 2. SIO 2019-2020

## Membres del grup
Grup 9:
- Sergio Candalija Valderrama
- Miquel Prats Segura

## Metodologia

Per obtenir la valoració que cada usuari pot haver-hi donat a cada restaurant ens em basat en les valoracions que altres usuaris han fet, s'han aplicat tècniques de veïnatge. En concret, s'han agrupat els usuaris en funció de la puntuació mitjana, és a dir, per a que un usuari sigui veí d'un altre, han de tindre una valoració mitja de +- 0,25 al usuari a estudiar. A continuació, es calcula la mitja de valoracions que han fet els usuaris per aquell restaurant. Aquest serà la valoració final del usuari.

## Resultat obtingut
La situació, a data del 28 de maig, és de la **cinquena**, amb un MAE de 3.4495

## Implementacions i configuracions

### Estrucutrua de la BD

#### users

| Field      | Type     | Null | Key | Default | Extra |
| - | - | - | - | - | - |
| User_name    | varchar(50) | NO  | PRI | NULL   |    |
| AvgValorations | float    | YES  |   | NULL   |    |

#### restaurant
| Field           | Type        | Null | Key | Default | Extra |
| - | - | - | - | - | - |
| Restaurant_name | varchar(50) | NO   | PRI | NULL    |       |

#### valorations
| Field | Type | Null | Key  | Default | Extra |
| ----- | ---- | ---- | ---- | ------- | ----- |
| User_name    | varchar(50) | NO  | PRI | NULL   |    |
| Restaurant_name | varchar(50) | NO  | PRI | NULL   |    |
| Valoration    | float    | NO  |   | NULL   |    |

#### UserData
| Field     | Type        | Null | Key | Default | Extra |
| ----- | ---- | ---- | ---- | ------- | ----- |
| User_name | varchar(50) | NO   | PRI | NULL    |       |
| Mitja     | float       | YES  |     | NULL    |       |
| Mediana   | float       | YES  |     | NULL    |       |
| Recompte  | int         | YES  |     | NULL    |       |
| Desv_pobl | float       | YES  |     | NULL    |       |
| Moda      | int         | YES  |     | NULL    |       |

#### RestaurantData
| Field           | Type        | Null | Key | Default | Extra |
| ----- | ---- | ---- | ---- | ------- | ----- |
| Restaurant_name | varchar(50) | NO   | PRI | NULL    |       |
| Mitja           | float       | YES  |     | NULL    |       |
| Mediana         | float       | YES  |     | NULL    |       |
| Recompte        | int         | YES  |     | NULL    |       |
| Desv_pobl       | float       | YES  |     | NULL    |       |
| Moda            | int         | YES  |     | NULL    |       |

#### Canvis des de la entrega anterior
Hem afegit la columna `AvgValorations` a la taula `users` a tráves de la consulta SQL

```sql
	UPDATE users u set AvgValorations=(SELECT AVG(Valoration) from valorations v where v.User_name =u.User_name)

```

Es poden inicialiltzar les taules amb `UserData` i `RestaurantData` amb `usersResults.py` i `restResults.py` respectivament.

