# Soluciones

#### Ejercicio 1
{name:"Babelgum"}
#### Ejercicio 2
{"number_of_employees":{$gt:5000}}
20
SORT {number_of_employees:1}
#### Ejercicio 3
{founded_year:{$in:[2000,2001,2002,2003,2004,2005]}}
Projection:{name:1, founded_year:1}
#### Ejercicio 4
{"ipo.valuation_amount":{$gte:100000000}, "founded_year":{$lte:2010}}
Projection:{name:1, ipo:1}
#### Ejercicio 5
{"number_of_employees":{$gt:1000}, "founded_year":{$lte:2005}}
10
SORT {number_of_employees:1}
#### Ejercicio 6
{companies:{$ne:"partners"}}
#### Ejercicio 7
{category_code:{ $type:'null'}}
#### Ejercicio 8
{"number_of_employees":{$gte:100}, "number_of_employees":{$lte:1000}}
Projection:{name:1, number of employees:1}
#### Ejercicio 9
companies
SORT {ipo:-1}
#### Ejercicio 10
companies
SORT {number_of_employees:-1}
10
#### Ejercicio 11
{founded_month:{$in:[1,2,3,4,5,6]}}
1000
#### Ejercicio 12
{"acquisition.price_amount":{$gte:10000000}, "founded_year":{$lte:2000}}
#### Ejercicio 13
{"acquisition.acquired_year":{$gt:2010}}
SORT{"acquisition.price_amount":-1}
Projection:{name:1, acquisition:1}
#### Ejercicio 14
companies
SORT {founded_year:-1}
Projection:{name:1, founded_year:1}
#### Ejercicio 15
{founded_day:{$in:[1,2,3,4,5,6,7]}, founded_month:{$eq:1}}
SORT {adquisition_price:-1}
LIMIT 10
#### Ejercicio 16
{category_code:{$eq:"web"}, "number_of_employees":{$gt:4000}}
SORT {"number_of_employees":1}
#### Ejercicio 17
{"acquisition.price_amount":{$gt:10000000}, "acquisition.price_currency_code":{$eq:'EUR'}}
#### Ejercicio 18
{"acquisition.acquired_month":{$in:[1,2,3]}}
10
Projection:{name:1, acquisition:1}
#### Ejercicio 19
{founded_year:{$gte:2000}, founded_year:{$lte:2010}, "acquisition.acquired_year":{$gt:2011}}
#### Ejercicio 20
{deadpooled_year:{$gt:3}}

