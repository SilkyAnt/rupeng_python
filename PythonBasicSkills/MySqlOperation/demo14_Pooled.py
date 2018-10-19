# 1、导入连接池的模块
import pymysql
from DBUtils.PooledDB import PooledDB,SharedDBConnection

# 2、创建一个连接池对象
pool = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    blocking=True,
    ping=1,

    host="172.3.8.90",
    user="root",
    password="您的数据库密码",
    database="students",
    charset="utf8"
)

print(pool)
conn1 = pool.connection()
print(conn1)
conn2 = pool.connection()
print(conn2)
conn3 = pool.connection()
print(conn3)
conn4 = pool.connection()
print(conn4)
conn5 = pool.connection()
print(conn5)
conn6 = pool.connection()
print(conn6)

# 这里的close方法，不会断开和数据库的连接，只是断开了和连接池的连接。
conn1.close()

