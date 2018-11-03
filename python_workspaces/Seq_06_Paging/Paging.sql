-- drop table if exists person;
create table person(id int primary key auto_increment,
name varchar(60) not null,
address varchar(60) not null
);
-- delete from person;
insert into person (name,address)
values ("梨花1","北京昌平1"),("梨花2","北京昌平2"),
("梨花3","北京昌平3"),("梨花4","北京昌平4"),
("梨花5","北京昌平5"),("梨花6","北京昌平6"),
("梨花7","北京昌平7"),("梨花8","北京昌平8"),
("梨花9","北京昌平9"),("梨花10","北京昌平10"),
("梨花11","北京昌平11"),("梨花12","北京昌平12"),
("梨花13","北京昌平13"),("梨花14","北京昌平14"),
("梨花15","北京昌平15"),("梨花16","北京昌平16"),
("梨花17","北京昌平17"),("梨花18","北京昌平18"),
("梨花19","北京昌平19"),("梨花20","北京昌平20");
-- select * from person;


/**
在mysql的SQL查询语句中,limit可以支持分页操作，第一个参数表示分页的开始（从0开始），
第二个参数表示查询数据的条数，比如如下SQL语句
   select * from person limit 5,3;
表示从第6条开始查询，往后查询3条数据。
结合封装类，改变两个参数的值即可实现分页功能。
sql="select * from person limit %s,%s"
p=PyMySQL()
lists=p.getManyData(sql,(3,6))
print(lists)
 */