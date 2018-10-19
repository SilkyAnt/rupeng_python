# 修改数据 注意：需要进行事务的处理
import pymysql
conn = pymysql.connect(host="172.3.8.90",port=3306,user="root",passwd="您的数据库密码",db="s1",charset="utf8")
cursor = conn.cursor()
try:
    rows = cursor.execute("update stu set s_address='广西桂林' where s_id = 2")
    conn.commit()
    if rows>=1:
        print("修改数据成功")
except:
    conn.rollback()
    print("修改数据失败")
cursor.close()
conn.close()