use test;
drop table stu;
create table stu(s_id int primary key,
s_name varchar(50) not null,
s_address varchar(60) default '北京昌平')
select * from stu;
insert into stu values(1,'李萍','北京海淀'),
(2,'刘华','上海红冲'),(3,'黄骅','深圳皇岗');
select * from  stu;

