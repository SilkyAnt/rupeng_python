# 通过python把图片（视频、文件等）存到数据库中
'''
脚本：
create table Images(img_id int primary key auto_increment,img longblob);
'''

import pymysql

conn = pymysql.connect(host="172.3.8.90",port=3306,user="root",passwd="您的数据库密码",db="students")
cursor = conn.cursor()
sql = "insert into images(img) values(%s)"

f = open("dog.png",mode="rb")
imageValues = f.read()
f.close()
try:
    cursor.execute(sql,imageValues)
    conn.commit()
except:
    conn.rollback()
finally:
    cursor.close()
    conn.close()
