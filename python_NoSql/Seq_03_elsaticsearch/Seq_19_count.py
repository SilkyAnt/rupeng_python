from elasticsearch import Elasticsearch

es = Elasticsearch()
# 执行查询并获取该查询的匹配数
# 获取数据量
result = es.count(index="my_index", doc_type="test_type")
print(result)
