create database registration_db;
use registration_db;

create table users(
primary_key int AUTO_INCREMENT primary key,
student_name varchar(100),
father_name varchar(100),
student_mother_name varchar(100),
date_of_birth DATE,
blood_group varchar(100),
password varchar(100)
);
alter table users
add column password varchar(100);

alter table users
add column phone_number int;

alter table users
add column email varchar(100);

alter table users
add column address varchar(100);

alter table users
add column department varchar(100);

alter table users
add column course varchar(100);

select * from users;







