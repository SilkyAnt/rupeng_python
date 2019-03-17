from elasticsearch import Elasticsearch

# 根据ID查询
es = Elasticsearch()
body = {
    "query": {
        "ids": {
            "type": "test_type",
            "values": [
                "1", "2", "3", "4"
            ]
        }
    }
}
# 搜索出id为1或2,3,4的所有数据
result2 = es.search(index="my_index", doc_type="test_type", body=body)
print(result2)
