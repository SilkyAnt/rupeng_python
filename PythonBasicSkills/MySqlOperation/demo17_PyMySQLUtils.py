# 封装python操作mysql的类
import pymysql
class PyMySQLUtils():
    # 初始化，获取连接对象
    def __init__(self,host="172.3.8.90",port=3306,user="root",passwd="您的数据库密码",db="students",charset="utf8"):
        self.host = host
        self.user = user
        self.port = port
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.conn = pymysql.connect(host=host,user=user,passwd=passwd,db=db,charset=charset)
        self.cursor = self.conn.cursor()

    # 返回连接对象
    def getConn(self):
        return self.conn

    # 返回游标
    def getCursor(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    # 查询出一个数据
    def getOneData(self, sql, param=None):
        cursor = self.conn.cursor()
        cursor.execute(sql, param)
        row = cursor.fetchone();
        cursor.close()
        return row

    # 查询出数据集
    def getManyData(self, sql, param=None):
        cursor = self.conn.cursor()
        cursor.execute(sql, param)
        row = cursor.fetchall();
        cursor.close()
        return row

    # 非查询操作:添加、删除、修改
    def noQury(self, sql, param=None):
        mark = False
        cursor = self.conn.cursor()
        cursor.execute(sql, param)
        try:
            self.conn.commit()
            mark = True
        except Exception as e:
            self.conn.rollback()
        finally:
            cursor.close()
        return mark

    # 关闭连接
    def closeAll(self):
        self.conn.close()

    # 销毁对象时，关闭连接
    def __del__(self):
        self.closeAll()

sql = "select count(1) from myTable"

utils = PyMySQLUtils()
row = utils.getOneData(sql)
print(row[0])