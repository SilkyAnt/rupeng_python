from elasticsearch import Elasticsearch
# 通过search方法查找
# 模糊批量查询
es = Elasticsearch()
result = es.search(index="my_index")
result2 = es.search(doc_type="stu")
print(result)
print(result2)
for r in result['hits']['hits']:
    print(r)
    print(r['_source'])