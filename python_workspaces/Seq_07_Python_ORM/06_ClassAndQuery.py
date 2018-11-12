import pymysql
import warnings
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, and_, or_, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()
warnings.filterwarnings("ignore")

engine = create_engine("mysql+mysqldb://root:您的数据库密码@172.3.8.234:3306/rupeng?charset=utf8", echo=True)
metadata = MetaData(engine)
Base = declarative_base()
DBSession = sessionmaker(bind=engine)
# 获取数据库和ORM框架之间的会话对象
session = DBSession()

'''
class User2(Base):
    __tablename__ = "user2"
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    address = Column(String(40))
# 建表
Base.metadata.create_all(engine)
# 删除表
# Base.metadata.drop_all(engine)
'''


# 创建表
class Stu(Base):
    __tablename__ = 'stus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), index=True)
    address = Column(String(16), nullable=False)


'''
# 创建表
Base.metadata.create_all(engine)
# 删除表
# Base.metadata.drop_all(engine)
# 添加数据

obj = Stu(name="alex0", address='北京昌平')
session.add(obj)
session.add_all([
    Stu(name="alex1", address='北京昌平'),
    Stu(name="alex2", address='北京海淀'),
    Stu(name="alex3", address='广东深圳'),
])
session.commit()
'''
ret = session.query(Stu).filter_by(name='alex1').all()
for r in ret:
    print(r.id)
r = session.query(Stu).filter(Stu.name == 'alex1').first()
print(r.id)
ret = session.query(Stu).filter(Stu.id > 2).all()
# between查询
ret = session.query(Stu).filter(Stu.id.between(1, 3)).all()
# in查询
ret = session.query(Stu).filter(Stu.id.in_([1, 3])).all()
# 取反
ret = session.query(Stu).filter(~Stu.id.in_([1, 3])).all()
# 子查询
ret = session.query(Stu).filter(Stu.id.in_(session.query(Stu.id).filter_by(name='alex1'))).all()
# and
ret = session.query(Stu).filter(and_(Stu.id >= 3, Stu.address == '北京海淀')).all()
# or
ret2 = session.query(Stu).filter(or_(Stu.id <= 2, Stu.address == '北京海淀')).all()
# 模糊查询
ret = session.query(Stu).filter(Stu.address.like('北京%')).all()
ret = session.query(Stu).filter(~Stu.address.like('北京%')).all()
# 限制:开始的下标值和结束的下标值
ret = session.query(Stu)[1:3]
# 分组
ret = session.query(Stu).group_by(Stu.address).all()
ret = session.query(
    func.max(Stu.id),
    func.sum(Stu.id),
    func.min(Stu.id)).all()
ret = session.query(
    func.max(Stu.id),
    func.sum(Stu.id),
    func.min(Stu.id)).group_by(Stu.address).all()

ret = session.query(
    func.max(Stu.id),
    func.sum(Stu.id),
    func.min(Stu.id)).group_by(Stu.address).having(func.min(Stu.id) >2).all()
print("%%%%%%%%")
for r in ret:
    print(r)

session.commit()
