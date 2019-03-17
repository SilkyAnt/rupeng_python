# ?用来匹配1个任意字符，*用来匹配零个或者多个字符
from elasticsearch import Elasticsearch

# 模糊查询
es = Elasticsearch()
body = {
    "query": {
        "wildcard": {
            "name": "python*"
        }
    }
}
# 模糊查询name包含python关键字的数据
result2 = es.search(index="my_index", doc_type="test_type", body=body)
print(result2)
