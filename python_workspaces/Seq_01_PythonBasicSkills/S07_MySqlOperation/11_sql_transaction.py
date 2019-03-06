# sql 事务的理解
# mysql 默认引擎 InnoDB 支持事务， MyISAM 引擎不支持事务
"""
-- 脚本
create table admin(
id int primary key,
name varchar(50) not null,
pwd varchar(60) not null
);
insert into admin values(1,'admin','123456');
"""

import pymysql

conn = pymysql.connect(host="172.3.8.90", port=3306, user="root", passwd="您的数据库密码", db="students", charset="utf8")
cursor = conn.cursor()  # 相当于开启事务
try:
    cursor.execute("insert into admin values(2,'admin','123456')")
    cursor.execute("insert into admin values(3,'admin','123456')")
    cursor.execute(r"insert into admin 我这行就写错的,前两行数据会回滚,插入无效")
    cursor.execute("insert into admin values(5,'admin','123456')")
    conn.commit()  # 相当于结束事务
except Exception as e:
    conn.rollback()
    print(e)
cursor.close()
conn.close()
