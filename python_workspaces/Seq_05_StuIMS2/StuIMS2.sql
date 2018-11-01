create table grade(
id int primary key auto_increment,
name varchar(40) not null
);
insert into grade(name) values("s1"),("s2"),("s3"),("s4");
-- select * from grade;

-- drop table stu_table;
create table stu_table(
id int primary key auto_increment,
name varchar(40) not null,
age int(3) not null,
gradeid int,
picture varchar(60) not null,
hobby varchar(80) not null,
sex varchar(10) not null,
foreign key(gradeid) references grade(id)
);

insert into stu_table(name,age,gradeid,picture,hobby,sex)
values("陈丽",23,4,"imgs/1.jpg","游泳,爬山","女"),
("刘华",18,3,"imgs/2.jpg","游泳,读书,阅读","男"),
("王丽",20,2,"imgs/3.jpg","爬山,游戏","女"),
("王郝丽",19,1,"imgs/4.jpg","阅读,游戏","女"),
("科德",23,2,"imgs/5.jpg","打游戏，玩蛇","男"),
("萨斯",18,2,"imgs/6.jpg","自行车，耍猴","男"),
("陈丞澄",20,3,"imgs/7.jpg","看书，看小说","女"),
("哈萨克",19,4,"imgs/8.jpg","网球，高尔夫球","女");

-- select * from stu_table;