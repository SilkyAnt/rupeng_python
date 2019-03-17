from elasticsearch import Elasticsearch

# 复合查询
# bool有3类查询关系，must(都满足),should(其中一个满足),must_not(都不满足)。
es = Elasticsearch()
body = {
    "query": {
        "bool": {
            "must": [
                {
                    "term": {
                        "name": "python"
                    }
                },
                {
                    "term": {
                        "age": 20
                    }
                }
            ]
        }
    }
}
# 获取name="python"并且age=20的所有数据
result = es.search(body=body)
print(result)
