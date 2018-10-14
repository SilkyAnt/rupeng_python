drop database students;
create database students;
use students;
drop table grade;
create table grade(
GRADEID int auto_increment primary key comment'grade表的主键',
GRADENAME varchar(50) comment '年级名称'
);
insert into grade values(28,'s28');
insert into grade values(29,'s29');
insert into grade values(30,'s30');

create table SUBJECT(
SUBJECTID int(10) auto_increment primary key comment'subject表的主键',
SUBJECTNAME varchar(50) comment '科目名称',
CLASSHOURS int(10),
GRADEID int(10),
 constraint id_fk foreign key(GRADEID) references grade(GRADEID)on delete cascade on update cascade
);

insert into SUBJECT values(1,'java',56,28);
insert into SUBJECT values(2,'html',66,29);
insert into SUBJECT values(3,'jsp',52,29);
insert into SUBJECT values(4,'javascript',36,30);
insert into SUBJECT values(5,'ssh',76,30);


drop table student;


create table  student(
STUDENTNO varchar(30)  primary key comment 'student表的主键',
PASSWORD varchar(50) default'123456' comment'学生的密码',
NAME varchar(50) comment'学生的名字',
GENDER varchar(2) comment'学生的性别',
GRADEID int(10) comment'年级编号，指向grade的GRADEID',
PHONE varchar(11),
ADDRESS varchar(100) default '北京海淀101号',
BIRTHDATE date comment '学生生日',
constraint stu_fk foreign key(GRADEID) references grade(GRADEID)on delete cascade on update cascade
);

select * from student;

insert into student values('10110110001',default,'徐长明','男',28,13867652948,'北京海淀101号','1991-05-01');
insert into student values('10110110010',default,'徐大猛','男',28,18170869527,'湖南长沙','1989-09-10');
insert into student values('10110110011',default,'曾小胖','男',30,13879103462,'江西吉安','1992-10-07');
insert into student values('10110110012',default,'刘莉莉','女',28,13667091782,'山东','1993-01-25');
insert into student values('10110110013',default,'熊大','男',28,18931034324,'安徽合肥','1987-05-15');
insert into student values('10110110014',default,'王珊','女',29,15128379408,'青岛','1995-07-07');
insert into student values('10110110015',default,'唐糖','女',30,19232950234,'四川','1995-07-07');
insert into student values('10110110016',default,'吴倩倩','女',30,15256749563,'青海','1990-03-21');
insert into student values('10110110017',default,'姜清','男',28,15534269565,'广东中山','1991-04-04');
insert into student values('10110110018',default,'龚建','男',29,18534657536,'广东珠海','1990-04-28');
insert into student values('10110110019',default,'姜易','男',28,13834264576,'重庆','1990-05-15');
insert into student values('10110110002',default,'王铭','男',29,15789762948,'湖北武汉','1991-08-12');
insert into student values('10110110020',default,'樊梨花','女',30,18335265892,'辽宁','1998-05-15');
insert into student values('10110110003',default,'刘丽','女',30,18734766894,'新疆乌鲁木齐','1980-02-03');
insert into student values('10110110004',default,'杜平','男',30,13725675673,'江西南昌','1992-04-08');
insert into student values('10110110005',default,'王楠','女',28,13265275673,'江西南昌','1990-02-01');
insert into student values('10110110006',default,'喻灰灰','女',29,13520850251,'江西南昌','1995-07-17');
insert into student values('10110110007',default,'肖星星','男',29,15970646829,'江西南昌','1986-07-15');
insert into student values('10110110008',default,'刘春','女',29,13177866852,'南昌潘家桥','1990-03-08');
insert into student values('10110110009',default,'小林子','男',30,1570378238,'广东','1991-06-28');

create table result(
ID int(12) auto_increment primary key comment'result表的主键',
STUDENTNO varchar(50) comment'学生学号，指向student表中的主键',
SUBJECTID int(10) comment'科目编号，指向科目表中的主键',
SCORE int(3) comment'该学生的某科目分数',
EXAMEDATE date comment'该学生的参加某科目的日期',
constraint stuNO_fk foreign key(STUDENTNO) references student(STUDENTNO)on delete cascade on update cascade,
constraint sub_fk foreign key(SUBJECTID) references SUBJECT(SUBJECTID)on delete cascade on update cascade
);
select * from result;

insert into result values(3,'10110110001',4,85,'2014-07-03');
insert into result values(4,'10110110004',5,78,'2014-07-04');
insert into result values(5,'10110110005',1,67,'2014-07-01');
insert into result values(6,'10110110006',1,83,'2014-07-01');
insert into result values(7,'10110110007',3,78,'2014-07-02');
insert into result values(8,'10110110008',2,79,'2014-07-02');
insert into result values(9,'10110110009',5,93,'2014-07-04');
insert into result values(10,'10110110010',2,83,'2014-07-02');
insert into result values(11,'10110110011',5,87,'2014-07-04');
insert into result values(12,'10110110012',1,82,'2014-07-01');
insert into result values(13,'10110110013',1,69,'2014-07-02');
insert into result values(14,'10110110014',3,85,'2014-07-02');
insert into result values(15,'10110110015',4,83,'2014-07-04');
insert into result values(16,'10110110016',1,83,'2014-07-03');
insert into result values(17,'10110110017',1,76,'2014-07-03');
insert into result values(18,'10110110018',3,86,'2014-07-02');
insert into result values(19,'10110110019',1,81,'2014-07-01');
insert into result values(20,'10110110020',5,88,'2014-07-04');

select  * from grade;
select * from student;
select * from subject;
select * from result;

