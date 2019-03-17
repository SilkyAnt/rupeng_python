from elasticsearch import Elasticsearch

# 批量操作
es = Elasticsearch()
doc = [
    # 创建一个_index=a,_type=b,_id=1，body={'name': 'jack', 'sex': 'male', 'age': 10 }的数据
    {'index': {'_index': 'a', '_type': 'b', '_id': '1'}},
    {'name': 'jack', 'sex': 'male', 'age': 10},
    # 删除一个_index=a,_type=b,_id=1的数据
    {'delete': {'_index': 'a', '_type': 'b', '_id': '1'}},
    # 创建一个_index=a,_type=b,_id=1，body={'name': 'lucy', 'sex': 'female', 'age': 20 }的数据
    {"create": {'_index': 'a', "_type": 'b', '_id': '2'}},
    {'name': 'lucy', 'sex': 'female', 'age': 20},
    # 修改一个'_index': 'a', '_type': 'b', '_id': '2'，body={'doc': {'age': '100'}}
    {'update': {'_index': 'a', '_type': 'b', '_id': '2'}},
    {'doc': {'age': '100'}}
]
result2 = es.bulk(index='a', doc_type='b', body=doc)
print(result2)
