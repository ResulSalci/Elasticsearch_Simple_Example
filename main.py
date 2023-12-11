from elasticsearch import Elasticsearch


es = Elasticsearch([{"host": "localhost", "port": 9200}])

result = es.get(index="products", doc_type="_doc", id=2)

source_data = result["_source"]

print(source_data)

source_data["amount"] = "2000"

es.index(index="products", doc_type="_doc", id=2, body= source_data)