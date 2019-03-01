# mysql 插入10W条数据正常需要的时间 1s
"""
-- 表结构
create table myTable(created_day date ,name varchar(40),count varchar(40));
"""

import pymysql
import time

conn = pymysql.connect(host="172.3.8.90", port=3306, user="root", passwd="您的数据库密码", db="students", charset="utf8")
cursor = conn.cursor()  # 相当于开启事务

try:
    begin = time.time()
    sql = "insert into myTable values(%s,%s,%s)"
    args = []
    for i in range(1, 100001):
        t = ('2018-09-14', 'name' + str(i), str(i))
        args.append(t)
    cursor.executemany(sql, args)
    conn.commit()  # 相当于结束事务
except Exception as e:
    conn.rollback()
    print(e)
finally:
    cursor.close()
    conn.close()
    end = time.time()
    print(end - begin)
