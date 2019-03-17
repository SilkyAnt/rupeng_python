from elasticsearch import Elasticsearch

#  库中并没有数据，代码执行报错，仅供参考
es = Elasticsearch()
body = {
    "query": {
        "match_all": {}
    },
    "aggs": {  # 聚合查询
        "sum_age": {  # 和的key
            "sum": {  # 求和
                "field": "age"  # 查询"age"的和
            }
        }
    }
}
# 搜索所有数据,获取age的和
result = es.search(index="stu_e", doc_type="tests", body=body)
print(result)
