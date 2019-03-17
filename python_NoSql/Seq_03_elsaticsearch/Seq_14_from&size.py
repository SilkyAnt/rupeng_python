from elasticsearch import Elasticsearch

# 切片查询，其实就是个范围
es = Elasticsearch()
body = {
    "query": {
        "match_all": {}
    },
    "from": 2,  # 从第二条数据开始
    "size": 4  # 获取4条数据
}
# 从第2条数据开始，获取4条数据
result = es.search(body=body)
print(result)
