# 查询所有数据
from elasticsearch import Elasticsearch
import json

es = Elasticsearch()
# 搜索所有数据
result = es.search(index="my_index", doc_type="test_type")
print(result)
# 或者
body = {
    "query": {
        "match_all": {}
    }
}
result2 = es.search(body=body)
print(json.dumps(result2, indent=2, ensure_ascii=False))
