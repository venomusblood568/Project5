/* practice. question 1*/
/*
Create a database for your company named XYZ.
Step1: create a table inside this DB to store employee info (id, name and salary).
Step2 : Add following information in the DB:
1, "adam", 25000
2, "bob", 30000
3, "casey", 40000
Step3 : Select & view all your table data.
*/
create database XYZ;

create TABLE store(
	id int primary key,
    name varchar(50),
	salary int not null
);

show tables;

insert into store 
(id,name,salary)
values 
(0,"adam",25000),
(1,"bob",30000),
(2,"casey",40000);

select * from store;
