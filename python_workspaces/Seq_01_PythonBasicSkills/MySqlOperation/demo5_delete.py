# 删除数据 注意：需要进行事务的处理
import pymysql

conn = pymysql.connect(host="172.3.8.90", port=3306, user="root", passwd="您的数据库密码", db="s1", charset="utf8")
cursor = conn.cursor()
try:
    rows = cursor.execute("delete from stu where s_id = 4")
    conn.commit()
    if rows >= 1:
        print("删除数据成功")
except:
    conn.rollback()
    print("删除数据失败")
cursor.close()
conn.close()
