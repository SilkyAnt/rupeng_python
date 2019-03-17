from elasticsearch import Elasticsearch

# 通过get方法查找
# 精确查找，三个属性都是必要的
es = Elasticsearch()
result = es.get(doc_type="test_type", index="my_index", id=1)
print(result)
print(result['_source'])
