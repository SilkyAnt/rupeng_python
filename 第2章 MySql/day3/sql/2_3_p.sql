select abs(-4);
select abs(4);
select bin(13);
select oct(13);
select hex(113);

select ceiling(-23.45);
select floor(23.45);
select exp(2);

select ln(7.38905609893065);
select log10(100);
select log(3,9);
select mod(12,5);
select greatest(23,45,67,123,256,732,90,1,3,1234);
select least(23,45,67,123,256,732,90,1,3,1234);

select PI();
select floor(10+rand()*90+1);

select round(123.4561789,3);
select sign(-4);
select sign(4);
select sign(0);

select sqrt(25);
select truncate(123.4569789,3);

select ascii('#');
select bit_length('2');
select length(concat("s1","s2","dhgsd",'s4djfhsdf'));
select concat_ws("s1","s2","dhgsd",'s4djfhsdf');
select insert("12345678",2,3,"abcdefg");
select find_in_set("asw","asa,sadqw,adsawqe,asw,121,sadas");
SELECT FIND_IN_SET('b','a,b,c,d'); 

select lower("asaSQWWAS");
select lcase("asaSQWWAS");


select ucase("asaSQWWAS");
select upper("asaSQWWAS");

select left("aswwq",2);
select right("aswwq",4);

select ltrim("   sajshdag");
select rtrim("   sajshdag    ");
select trim("   sajshdag    ");

select POSITION('sa' in '1234saufdfsad');
select repeat("abc",3);
select reverse("123422424");
select strcmp("1b","1a");


select current_date();
select current_time();
select current_timestamp();
select now();

select date_add(CURRENT_DATE,INTERVAL 3 day);
SELECT DATE_ADD(CURRENT_DATE,INTERVAL 6 MONTH);

select date_sub(CURRENT_DATE,INTERVAL 3 day);
select date_format(now(),'%Y年%m月%d日');

select DAYOFYear(now());
SELECT DAYNAME(CURRENT_DATE);
select monthname(CURRENT_DATE());
select quarter(CURRENT_DATE());

select minute(now());
select hour(now());
select second(now());
select week(now());
select year(now());
select month(now());
select day(now());
-- 抽取
SELECT EXTRACT(YEAR_MONTH FROM CURRENT_DATE);
SELECT EXTRACT(DAY_SECOND FROM now());
SELECT EXTRACT(HOUR_MINUTE FROM now());

SELECT PERIOD_DIFF(200302,199802);


select sysdate();

select str_to_date("1998-12-12","%Y-%m-%d");
select str_to_date('14:47:23', '%H:%i:%s');
select str_to_date('08:09:30', '%h:%i:%s'); 

select date_format(now(),"%Y年%m月%d日 %H:%i:%s");

select aes_encrypt("hello",23);
select AES_ENCRYPT("hello",23);

select AES_DECRYPT(AES_ENCRYPT("hello",23),23);
SELECT ENCODE('xufeng','key');
SELECT DECODE(ENCODE('xufeng','key'),'key');
SELECT MD5('123456');
SELECT SHA('123456');




select format(1234.5678,2);

SELECT DATE_FORMAT(NOW(),'%W,%D %M %Y %r');
SELECT DATE_FORMAT(NOW(),'%Y-%m-%d');
SELECT DATE_FORMAT(19990330,'%Y-%m-%d');
SELECT DATE_FORMAT(NOW(),'%h:%i %p');

SELECT INET_ATON('10.122.89.47');
SELECT INET_NTOA(175790383);

SELECT CAST(NOW() AS SIGNED INTEGER),CURDATE()+2;
SELECT CAST('F' AS BINARY);

select database();
select user();
select system_user();
select version();

select * from mysql.user ;
SELECT USER();

select * from mysql.user where user="root";

show grants;
-- mySQl的用户管理
-- 1、创建一个用户
drop user 'afeng';
create user 'afeng' identified by 'afeng';
insert into mysql.user(host,user, authentication_string,ssl_cipher,x509_issuer,x509_subject)
values('%',"czf",password("czf"),"","","");

drop user 'afeng';
drop user 'czf';

grant select,update,delete,insert on test.* to afeng;
revoke update,delete,insert on test.* from afeng;

update mysql.user set authentication_string=password("123456")
where user='afeng';

select * from mysql.user;






