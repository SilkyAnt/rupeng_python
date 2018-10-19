# sql注入 的解决方法
# 使用pymysql提供的参数化语句防止注入
'''
-- 脚本
create table admin(
id int primary key,
name varchar(50) not null,
pwd varchar(60) not null
);
insert into admin values(1,'admin','123456');
-- 登录的时候
帐号输入： ' or 1=1 --
密码输入以及不输入，都能登录成功
'''

import pymysql
conn = pymysql.connect(host="172.3.8.90",port=3306,user="root",passwd="您的数据库密码",db="students",charset="utf8")
cursor=conn.cursor()
name=input("请输入用户名:")
pwd=input("请输入密码:")
cursor.execute("select count(*) from admin where name=%s  and pwd=%s ",(name,pwd))
rows=cursor.fetchone()
print(rows[0])
if rows[0] >= 1:
    print("登录成功")
else:
    print("登录失败!")
cursor.close()
conn.close()