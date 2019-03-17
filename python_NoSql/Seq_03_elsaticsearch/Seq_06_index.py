from elasticsearch import Elasticsearch

# 创建索引
es = Elasticsearch()
result = es.indices.create(index='news2', ignore=400)
print(result)

# 删除索引
result2 = es.indices.delete(index='news2', ignore=[400, 404])
print(result2)
