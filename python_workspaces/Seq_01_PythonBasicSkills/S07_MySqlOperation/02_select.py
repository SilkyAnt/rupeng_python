# 遍历某个表的所有数据
import pymysql

conn = pymysql.connect(host="172.3.8.90", port=3306, user="root", passwd="您的数据库密码", db="students", charset="utf8")
cursor = conn.cursor()
cursor.execute("select * from student")
rows = cursor.fetchall()
for r in rows:
    print(r)

cursor.close()
conn.close()
