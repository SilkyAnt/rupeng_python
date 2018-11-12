from sqlalchemy import create_engine
# python3.*报“ImportError: No module named ‘MySQLdb'”
# 参考连接：https://www.cnblogs.com/TaleG/p/6735099.html
# 因为 MySQLdb只支持Python2.*，还不支持3.*
# 所以需要在项目中 引入下面两行代码
# 或者在项目的 __init__.py文件中加入和两行语句。
# 另一种解释：
# 参考链接：https://blog.csdn.net/zoulonglong/article/details/79539626?tdsourcetag=s_pctim_aiomsg
# python2和python3在数据库模块支持这里存在区别，python2是mysqldb
# 而到了python3就变成mysqlclient，pip install mysqlclient即可。
import pymysql
pymysql.install_as_MySQLdb()

# 使用 sqlalchemy 连接数据库
engine = create_engine("mysql+mysqldb://root:您的数据库密码@172.3.8.234:3306/rupeng?charset=utf8",echo=True)
print(engine)