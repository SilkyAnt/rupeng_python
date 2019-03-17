from elasticsearch import Elasticsearch

# 默认host为localhost,port为9200.但也可以指定host与port
es = Elasticsearch()
# 获取索引为my_index,文档类型为test_type的所有数据,result为一个字典类型
# 通过update修改之后，_version 也会对应改变
result = es.search()
print(result)
es.update(index="my_index", doc_type="test_type", id=1, body={"doc": {"name": "python1", "addr": "深圳1"}})
result2 = es.get(index='my_index', doc_type='test_type', id=1)
print(result2)
