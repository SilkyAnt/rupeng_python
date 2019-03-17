from elasticsearch import Elasticsearch

# 根据正则表达式查询
es = Elasticsearch()
body = {
    "query": {
        "regexp": {
            "name": "python[0-9]{0,3}"
        }
    }
}
# 正则查询name包含python，并包含0到3个数字数据
result2 = es.search(index="my_index", doc_type="test_type", body=body)
print(result2)
