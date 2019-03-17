from elasticsearch import Elasticsearch

es = Elasticsearch(['localhost:9200'])

results = es.search()
print(results)
# result = es.delete(index="my_index", doc_type="test_type", id='1')
