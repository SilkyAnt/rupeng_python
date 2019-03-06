# 从数据库中读取图片
"""
脚本：
create table Images(img_id int primary key auto_increment,img longblob);
"""

import pymysql

conn = pymysql.connect(host="172.3.8.90", port=3306, user="root", passwd="您的数据库密码", db="students")
cursor = conn.cursor()
sql = "select  img from images where img_id = 1"

cursor.execute(sql)
img = cursor.fetchone()[0]
f2 = open("dog.jpg", mode="wb")
f2.write(img)
f2.close()
print(img)
cursor.close()
conn.close()
