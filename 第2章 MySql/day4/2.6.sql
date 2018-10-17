/**
1、自然查询 
**/
use students;
select * from grade;
select gradeid from grade where gradename='s28';
select * from student where GRADEID=28;

select * 
from student s ,grade g
where g.GRADENAME='s28'
and s.GRADEID=g.GRADEID;

select s.name,s.phone
from student s,grade g
where g.gradename='s29'
and s.gradeid=g.gradeid;

select *
from student s,grade g
where s.gender='女' and
g.GRADENAME='s28'
and s.GRADEID=g.GRADEID;

select sub.SUBJECTID,sub.SUBJECTNAME,sub.CLASSHOURS,g.GRADENAME
from subject sub,grade g
where CLASSHOURS>=60
and sub.GRADEID=g.GRADEID;

select sub.subjectname
from subject sub,grade g
where g.gradename='s29'
and sub.gradeid=g.gradeid;

select * from subject;

select s.NAME,s.ADDRESS
from student s,grade g
where s.GENDER='男'
and s.GRADEID=g.GRADEID
and g.GRADENAME='s29';


select ifnull(null,1);
select ifnull(2,1);
select if(1>0,"OK","error");


create table pet(
name varchar(50), 
health int(5) ,
status int(2)
);
insert into pet values(null,100,1);
insert into pet values('贝贝',100,1);
insert into pet values('美眉',100,2);


select * from pet;


select ifnull(name,"无名") as '宠物的名字',
health as '宠物的健康值',if(status=1,'正常','禁止') as '宠物的状态'
from pet;

-- 模糊查询
-- 1、查询所有刘姓的同学 
select * 
from student 
where name like '刘%';

-- 2、查询所有北京的同学 
select * 
from student 
where address like '%江西%';

-- 3、查询所有刘姓的同学 
select * 
from student 
where name like '刘_';
-- 4、查询所有刘姓的同学 
select * 
from student 
where name regexp '刘[丽春]';

-- 5、查询分数在60-80
select * 
from  result 
where score
between 67 and 79;

select * 
from  result 
where score>67
and score<79;

-- 查询所有年级编号为28,29的学生信息 
select *
from student
where gradeid in(28,29);

select *
from student
where gradeid=28 or gradeid=29;

select  s.name,s.phone,s.address
from student s
where s.address like '%山东%';

select * from subject
where SUBJECTNAME like '%java%';

select * 
from student
where phone like '1387%';

select * 
from student
where name like '姜_';

select * from subject
where subjectid in(1,2);

select * 
from subject
where CLASSHOURS 
between 60 and 70;

select * 
from  student
where birthdate between '1991-01-01' and '2000-12-12';
/**
聚合函数 
**/
select * from result;
select * from subject;


-- 1、统计有多少学生 
select count(*) from student;
select count(*) from result;
-- 2、统计考试科目为java的总分 
select sum(r.score) 
from result r,subject sub
where sub.SUBJECTNAME='java'
and r.SUBJECTID=sub.SUBJECTID
-- 3、统计考试科目为java的平均分 
select avg(r.score) 
from result r,subject sub
where sub.SUBJECTNAME='java'
and r.SUBJECTID=sub.SUBJECTID;

-- 4、统计参加考试科目为java的学生人数
select count(r.score) 
from result r,subject sub
where sub.SUBJECTNAME='java'
and r.SUBJECTID=sub.SUBJECTID

-- 4、统计参加考试科目为java的最高分
select max(r.score) 
from result r,subject sub
where sub.SUBJECTNAME='java'
and r.SUBJECTID=sub.SUBJECTID;
-- 5、统计参加考试科目为java的最低分
select min(r.score) 
from result r,subject sub
where sub.SUBJECTNAME='java'
and r.SUBJECTID=sub.SUBJECTID;
-- 6、统计及格人数 
select count(*)
from result
where score>=70;

select count(*)
from result;

-- 查询S28年级的总学时
select * from grade;
select * from subject;

select sum(s.classhours)
from subject s,grade g
where g.GRADENAME='s28'
and s.GRADEID=g.GRADEID;


select count(*) as '人数',g.gradename as '年级名称'
from student s,grade g
where s.GRADEID=g.GRADEID
group by g.gradename;

select avg(r.score), sub.SUBJECTNAME
from result r,subject sub
where r.SUBJECTID=sub.SUBJECTID
group by sub.SUBJECTNAME
order by avg(r.score) ;


select * from subject;

select sum(sub.classhours),g.GRADENAME
from subject sub,grade g
where sub.gradeid=g.GRADEID
group by g.GRADENAME
order by sum(sub.classhours);

select avg(r.SCORE),r.STUDENTNO
from result r
group by r.STUDENTNO;

select avg(r.score),r.subjectid
from result r
group by r.subjectid
order by avg(r.score);

select * from result;

select sum(r.score),r.STUDENTNO
from result r
group by r.STUDENTNO
order by sum(r.score);


select count(*) as '人数', gradeid as '年级编号',gender as '性别'
from student
group by gradeid,gender;


select count(*),s.GRADEID
from student s
group by s.GRADEID
having count(*)>6;

-- 统计不同年级的超过25岁的学生人数
select count(*),g.gradeid
from student s,grade g
where ((to_days(sysdate())-to_days(s.BIRTHDATE)))/365>=25
and s.GRADEID=g.GRADEID
group by g.gradeid;

select * from student;

select ((to_days(sysdate())-to_days(s.BIRTHDATE)))/365
from student s;


select count(*),g.GRADENAME
from result r,grade g,subject sub
where r.score
between 60 and 70
and r.SUBJECTID=sub.SUBJECTID and sub.GRADEID=g.GRADEID
group by g.GRADENAME;


select * from result;

/**
1、内联查询 
**/
-- 1、查询所有年级名称为s29的学生信息 
select  s.*,g.GRADENAME
from student s,grade g
where g.GRADENAME='s29' 
and s.GRADEID=g.GRADEID;

select  s.*,g.GRADENAME
from student s
inner join grade g
on s.GRADEID=g.GRADEID
and g.GRADENAME='s29';

select * from result;
-- 1、查询学生的姓名、性别、所在的年级名称，
-- 参加的考试科目和对应的分数。
select s.name,s.gender,g.GRADENAME,sub.SUBJECTNAME,r.SCORE
from student  s
inner join grade g
on s.gradeid=g.gradeid
inner join subject sub
on sub.GRADEID=g.GRADEID
inner join result r
on r.SUBJECTID=sub.SUBJECTID
and r.STUDENTNO=s.STUDENTNO















