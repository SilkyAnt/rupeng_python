from elasticsearch import Elasticsearch

# 前缀查询
es = Elasticsearch()
body = {
    "query": {
        "prefix": {
            "name": "李"
        }
    }
}
# 查询前缀为"李"的所有数据
result = es.search(body=body)
print(result)
