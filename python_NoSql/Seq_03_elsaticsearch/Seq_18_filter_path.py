from elasticsearch import Elasticsearch

# 代码不能执行，真正需要用到再研究
es = Elasticsearch()
body = {}
# 只需要获取_id数据,多个条件用逗号隔开
es.search(index="my_index", doc_type="test_type", filter_path=["hits.hits._id"])
# 获取所有数据
es.search(index="my_index", doc_type="test_type", filter_path=["hits.hits._*"])
# 只需要获取_id,_source数据,多个条件用逗号隔开
result = es.search(index="stu_e", doc_type="tests", body=body, filter_path=["hits.hits._id,hits.hits._source"])
