from elasticsearch import Elasticsearch

es = Elasticsearch()
body = {
    "query": {
        "term": {
            "name": "python1"
        }
    }
}
# 查询name="python1"的所有数据
result2 = es.search(body=body)
print(result2)
# terms
body = {
    "query": {
        "terms": {
            "name": [
                "python1", "python"
            ]
        }
    }
}
# 搜索出name="python1"或name="python"的所有数据
result2 = es.search(index="my_index", doc_type="test_type", body=body)
print(result2)
