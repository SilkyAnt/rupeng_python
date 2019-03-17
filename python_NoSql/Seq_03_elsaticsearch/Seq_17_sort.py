from elasticsearch import Elasticsearch

# 排序
es = Elasticsearch()
body = {
    "query": {
        "match_all": {}
    },
    "sort": {
        "age": {  # 根据age字段升序排序
            "order": "asc"  # asc升序，desc降序
        }
    }
}
result = es.search(index="stu_e", doc_type="tests", body=body)
print(result)
