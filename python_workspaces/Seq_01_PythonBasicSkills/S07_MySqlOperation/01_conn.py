"""
1、安装PyMysql
2、导入PyMysql模块
3、创建连接对象
4、由连接对象获取游标对象
5、由游标对象执行sql语句
6、在游标对象中获取结果
7、关闭资源（包括游标和连接对象）
"""
import pymysql

conn = pymysql.connect(host="172.3.8.90", port=3306
                       , user='root', passwd='您的数据库密码', db='s1')

cursor = conn.cursor()
cursor.execute("select count(1) from stu")
counts = cursor.fetchone()
print(counts[0])
cursor.close()
conn.close()
