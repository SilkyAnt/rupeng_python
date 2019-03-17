# encoding = utf-8
from elasticsearch import Elasticsearch

# 添加数据有两种方法  index 和 create
# 默认host为localhost,port为9200.但也可以指定host与port
es = Elasticsearch()
# 添加或更新数据,index，doc_type名称可以自定义，id可以根据需求赋值,body为内容
es.index(index="my_index", doc_type="test_type", id=1, body={"name": "python", "addr": "深圳"})
# 或者:ignore=409忽略文档已存在异常
es.create(index="my_index", doc_type="test_type", id=1, ignore=409, body={"name": "python", "addr": "深圳"})
body = {"stu1": {"name": 'lucy', 'sex': 'female', 'age': 10}, "stu2": {"name": 'lucy2', 'sex': 'male', 'age': 12}}
# 需要注意的是，索引名必须小写
es.index(index='stu', doc_type='stu', body=body, id=2)
