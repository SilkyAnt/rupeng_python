# 查询数据  传参：字典
import pymysql
conn = pymysql.connect(host="172.3.8.90",port=3306,user="root",passwd="您的数据库密码",db="students",charset="utf8")
cursor = conn.cursor()
num = input("请输入要查询的学生学号：")
sql = "select * from student where STUDENTNO = %(id)s"
args = {"id":num}
cursor.execute(sql,args)
rows = cursor.fetchall()
for r in rows:
    print(r)

cursor.close()
conn.close()