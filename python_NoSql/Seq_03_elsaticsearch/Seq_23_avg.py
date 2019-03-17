from elasticsearch import Elasticsearch

#  库中并没有数据，代码执行报错，仅供参考
es = Elasticsearch()
body = {
    "query": {
        "match_all": {}
    },
    "aggs": {  # 聚合查询
        "avg_age": {  # 平均值的key
            "avg": {  # 求平均值
                "field": "age"  # 查询"age"的平均值
            }
        }
    }
}
# 搜索所有数据,获取age的平均值
result = es.search(index="stu_e", doc_type="tests", body=body)
print(result)
