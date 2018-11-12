# 这个只是示范，并不能成功运行
# encoding=utf8
# 导入:
import pymysql
from sqlalchemy import create_engine

pymysql.install_as_MySQLdb()

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:root@localhost:3306/blog?charset=utf8', echo=True)
conn = engine.connect()
# 开启事务
trans = conn.begin()
try:
    r1 = conn.execute("select * from usertable")
    for r in r1:
        print(r[0], r[1], r[2])
    conn.execute("insert into userTable values(131,'afeng','liu afeng')")
    # 事务提交
    trans.commit()
except:
    # 事务回滚
    trans.rollback()
    raise
