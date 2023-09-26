/*
For tine giver tabl,. ind the told payment according to each payment metinod.
*/

create database payment_company;

use payment_company;

create TABLE payments(
cust_id int primary key,
name varchar(50),
mode  varchar(50) NOT NULL,
city varchar(50) NOT NULL 
);

INSERT into payments
(cust_id,name,mode,city)
VALUES
(101,"olivia","netbanking","portland"),
(102,"ethan","credit card","miami"),
(103,"maya","credit card","seattle"),
(104,"liam ","netbanking","denver"),
(105,"sophia","credit card","new orleans"),
(106,"caleb","debit card","minneapolis"),
(107,"ava","debit card","phoenix"),
(108,"lucas","netbanking","bostan"),
(109,"isabella","netbanking","nashville"),
(110,"jackson","credit card","boston");

select * from payments;

SELECT mode , count(name) 
from payments
group by mode;
