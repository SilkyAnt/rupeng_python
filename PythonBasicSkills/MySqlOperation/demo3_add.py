# 插入数据 注意：需要进行事务的处理
import pymysql
conn = pymysql.connect(host="172.3.8.90",port=3306,user="root",passwd="您的数据库密码",db="s1",charset="utf8")
cursor = conn.cursor()
try:
    rows = cursor.execute("insert into stu values(2,'支成丽','广东广州')")
    conn.commit()
    if rows>=1:
        print("插入数据成功")
except:
    conn.rollback()
    print("插入失败")
cursor.close()
conn.close()