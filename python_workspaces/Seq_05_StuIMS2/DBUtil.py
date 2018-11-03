# 1、导入模块
import pymysql


class PyMySQL:
    # 初始化，获取连接对象
    def __init__(self, host="172.3.8.234", port=3306, user="root", passwd="您的数据库密码", db="rupeng", charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.conn = pymysql.connect(host=host, port=int(port), user=user, passwd=passwd, db=db, charset=charset)

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
        row = cursor.fetchone()
        cursor.close()
        return row

    # 查询出数据集
    def getManyData(self, sql, param=None):
        cursor = self.conn.cursor()
        cursor.execute(sql, param)
        row = cursor.fetchall()
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
