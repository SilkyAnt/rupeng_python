# 模糊查询
import pymysql
conn = pymysql.connect(host="172.3.8.90",port=3306,user="root",passwd="您的数据库密码",db="students",charset="utf8")
cursor = conn.cursor()
gender = input("请输入要查询的学生性别：")
address = input("请输入要查询的学生模糊地址：")
sql = r"select * from student where gender = %s and address like %s"
args = [gender,"%"+str(address)+"%"]
cursor.execute(sql,args)
rows = cursor.fetchall()
for r in rows:
    print(r)

cursor.close()
conn.close()