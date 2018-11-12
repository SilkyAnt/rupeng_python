# python3.*报“ImportError: No module named ‘MySQLdb'”
# 参考连接：https://www.cnblogs.com/TaleG/p/6735099.html
# 因为 MySQLdb只支持Python2.*，还不支持3.*
# 所以需要在项目中 引入下面两行代码
# 或者在项目的 __init__.py文件中加入和两行语句。
# import pymysql
# pymysql.install_as_MySQLdb()
# 另一种解释：
# 参考链接：https://blog.csdn.net/zoulonglong/article/details/79539626?tdsourcetag=s_pctim_aiomsg
# python2和python3在数据库模块支持这里存在区别，python2是mysqldb
# 而到了python3就变成mysqlclient，pip install mysqlclient即可。
import pymysql
import warnings
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String

pymysql.install_as_MySQLdb()
# 把警告给忽略掉
warnings.filterwarnings("ignore")

# 使用 sqlalchemy 连接数据库 并且建表
# echo 是控制 sql 语句的输出
engine = create_engine("mysql+mysqldb://root:您的数据库密码@172.3.8.234:3306/rupeng?charset=utf8", echo=True)


# 给表 user 新增数据
def insertUser():
    return "insert into user(id,name,address) " \
           "values(1,'czf','北京昌平'),(2,'czf','北京昌平'),(3,'czf','北京昌平')"


# 给表 user 删除数据
def deleteUser(id):
    return "delete from user where id = " + str(id)


# 修改表 user 中的数据
def updateUser():
    return "update user set name = %s where id = %s"


# 查询表中的数据
def queryUser():
    sql = "select * from user"
    list1 = engine.execute(sql)
    for row in list1:
        print(row[0], row[1], row[2])


# engine.execute(insertUser())
# engine.execute(deleteUser(3))
engine.execute(updateUser(), ("czf123", "1"))
queryUser()

# 以上是无连接对象的连接，不支持事务
# conn = engine.connect() 的方式是有连接，支持事务
# 之后执行代码使用 conn.execute(sql)

