from elasticsearch import Elasticsearch

es = Elasticsearch()
# match:匹配name包含python关键字的数据
body = {
    "query": {
        "match": {
            "name": "python"
        }
    }
}
# 查询name包含python关键字的数据
result2 = es.search(index="my_index", doc_type="test_type", body=body)
print(result2)
# multi_match:在name和addr里匹配包含深圳关键字的数据
body = {
    "query": {
        "multi_match": {
            "query": "深圳",
            "fields": ["addr", "name"]
        }
    }
}
# 查询name和addr包含"深圳"关键字的数据
result2 = es.search(index="my_index", doc_type="test_type", body=body)
print(result2)
