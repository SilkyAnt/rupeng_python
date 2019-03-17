from elasticsearch import Elasticsearch

# 范围查询
es = Elasticsearch()
body = {
    "query": {
        "range": {
            "age": {
                "gte": 18,  # >=18
                "lte": 30  # <=30
            }
        }
    }
}
# 查询18<=age<=30的所有数据
result = es.search(body=body)
print(result)
