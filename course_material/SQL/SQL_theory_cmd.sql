/* for creating database */
CREATE DATABASE trial_db;

create database college;

/* for droping db */
drop database trial_db;

/* for using db and applying the command */
use college;

/* for creating table naming student with id,name,age */
CREATE TABLE student(
id int primary key, 
name varchar(50),
age int not null
);

/* for inserting the values in the table */
INSERT into student values(01,"sam",21); 
INSERT into student values(02,"gourav",21); 

/* for seeing all the values */
select * from student;

/* for types of values 
CAHR, VARCHAR, BLOB, INT, TINYINT, BIGINT, BIT, FLOAT, DOUBLE, BOOLEAN, DATE, YEAR
CHAR = string(0-255), can store characters of fixed length
VARCHAR = string(0-255), can store characters up to given length
*/

/* SIGNED = where values can be both +ve or -ve eg(TINYINT UNSIGNED(50))
   UNSIGNED = where values can be only +ve */
   
/*
Types of SQL Commands
DDL (Data Definition Language) : create, alter, rename, truncate & drop
DQL (Data Query Language) : select
DML (Data Manipulation Language) : insert, update & delete
DCL (Data Control Language) : grant & revoke permission to users
TCL (Transaction Control Language) : start transaction, commit, rollback
*/

/* if exits command*/
create database if not exists college;

/* for droping the db is exists*/
drop database if exists trial_db;

/* for seeing all the database */
show databases;

/* for seeing all the tables */
show tables; 


/* middle data got delete you can refer the pdf */











/* truncate = for deleting the data of tabel drop will delet the whole table  */
/*
SQL JOIN = ven diagram
types = inner join , left join ,right join , full join 


*/

CREATE database sky;
use sky;
create table student_sky(
id int primary key,
name_ varchar(50)
);

insert into student_sky(id,name_ )
values 
(101, "adam"), 
(102, "bob"), 
(103, "casey");

create table course_sky(
id int primary key,
course varchar (50)
);

insert into course_sky(id,course)
values 
(102, "english"), 
(105, "math"), 
(103, "science"), 
(107, "computer science");

/* inner join syntax*/
SELECT *
FROM student_sky
INNER JOIN course_sky
ON student_sky.id = course_sky.id;

