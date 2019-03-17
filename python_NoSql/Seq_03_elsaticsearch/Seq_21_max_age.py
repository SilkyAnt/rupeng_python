from elasticsearch import Elasticsearch

#  库中并没有数据，代码执行报错，仅供参考
es = Elasticsearch()
body = {
    "query": {
        "match_all": {}
    },
    "aggs": {  # 聚合查询
        "max_age": {  # 最大值的key
            "max": {  # 最大
                "field": "age"  # 查询"age"的最大值
            }
        }
    }
}
# 搜索所有数据，并获取age最大的值
result = es.search(index="stu_e", doc_type="tests", body=body)
print(result)
