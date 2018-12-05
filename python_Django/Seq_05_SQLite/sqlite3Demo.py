import sqlite3

# 该文件路径可以是绝对路径，例如 C:/jianglp.sqlite3
conn = sqlite3.connect(r"db.sqlite3")
c = conn.cursor()


# 建表
def createTable():
    createTable = """CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL)"""
    c.execute(createTable)


# 初始化数据
def insertData():
    # 插入数据
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00 )")
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")


# 查询数据
def queryTable():
    rows = c.execute("SELECT id, name, address, salary  from COMPANY")
    for row in rows:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")


# 修改数据
def updateData():
    c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
    conn.commit()


# 删除数据
def deleteData():
    c.execute("DELETE from COMPANY where ID=2;")
    conn.commit()


createTable()
insertData()
# updateData()
# deleteData()
queryTable()

conn.commit()
c.close()
