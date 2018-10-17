-- 1、复习内联 
-- 查询性别为女，年级为s28的学生信息 
use students;
select s.*
from student s
inner join grade g
on s.GRADEID=g.GRADEID
and s.GENDER='女'
and g.GRADENAME='s28';

select * from student;
select * from grade;
insert into grade values(31,'s31');
-- 查询学生的姓名和所在的年级名称  
 
select s.NAME,g.GRADENAME
from student s
inner join grade g
on s.GRADEID=g.GRADEID;
-- 查询年级名称和它对应的学生姓名 
select g.GRADENAME,s.NAME
from grade g left outer join  student s
on s.GRADEID=g.GRADEID;
 -- 统计每个年级的学生人数
 select g.GRADENAME,count(*)  as '人数'
 from grade g 
 left join student s
 on s.GRADEID=g.GRADEID
 group by g.GRADENAME;
 
  select s.*
 from grade g 
 inner join student s
 on s.GRADEID=g.GRADEID
 and g.GRADENAME='s31';
  
 
 select * from subject;
 select * from result;
 select sub.SUBJECTNAME,r.score
 from subject sub
 left join result r
 on sub.subjectid=r.subjectid;
 
 select *
 from student
 where birthdate<(select birthdate
 from student
 where name='王珊') ;
 
 select birthdate
 from student
 where name='王珊';
 
-- 查询“jsp”课程至少一次考试刚好等于78分的学生
select s.*,sub.SUBJECTNAME,r.score
from student s
inner join result   r
on s.STUDENTNO=r.STUDENTNO
inner join subject sub
on r.SUBJECTID=sub.SUBJECTID
and sub.SUBJECTNAME='jsp' 
and r.score=78;

select s.*
from student s
where s.STUDENTNO=(select r.studentno 
from  result r where r.subjectid=(select sub.subjectid
 from subject sub where sub.subjectname='jsp') and r.score=78
);
# 查询参加最近一次“ssh”考试成绩最高分和最低分
select * from result;
select * from subject;

select max(r.score),min(r.score)
from result r
where r.SUBJECTID=(
select sub.subjectid from subject sub
where sub.SUBJECTNAME='ssh')
and r.EXAMEDATE=(
select max(EXAMEDATE) from result where  r.SUBJECTID=(
select sub.subjectid from subject sub
where sub.SUBJECTNAME='ssh') );

select s.name
from student s
where s.STUDENTNO not in (select r.STUDENTNO
from result r
where r.SUBJECTID=(
select sub.subjectid from subject sub
where sub.SUBJECTNAME='ssh')
and r.EXAMEDATE=(
select max(EXAMEDATE) from result where  r.SUBJECTID=(
select sub.subjectid from subject sub
where sub.SUBJECTNAME='ssh') ));

-- 查询s28学期开设的课程

select sub.*
from subject sub
where sub.GRADEID=(
select g.GRADEID 
from grade g 
where g.GRADENAME='s28'
);

-- 查询出学生的名字、科目名称、分数、所在的年级名称 
select s.name,sub.subjectname,r.score,g.gradename
from student s,subject sub,result r,grade g
where s.STUDENTNO=r.STUDENTNO
and sub.SUBJECTID=r.SUBJECTID
and g.GRADEID=s.GRADEID;


select s.name,sub.subjectname,r.score,g.gradename
from student s
inner join result r
on s.STUDENTNO=r.STUDENTNO
inner join subject sub
on sub.SUBJECTID=r.SUBJECTID
inner join grade g
on g.GRADEID=sub.GRADEID;

SELECT a.* FROM student as a 
inner JOIN student as b 
on a.BIRTHDATE<b.BIRTHDATE
and b.NAME='唐糖'













 
 






