from datetime import datetime
from elasticsearch import Elasticsearch
from random_employee import generate_ceo
from random_employee import generate_cto
from random_employee import generate_employee

es = Elasticsearch(
    ['http://localhost:9200'],
    # no verify SSL certificates
    verify_certs=False,
    # don't show warnings about ssl certs verification
    ssl_show_warn=False
)


for i in range(0,6):
    index_name = "test-index" + str(datetime.now().year) + str(datetime.now().month-i)
    print(index_name)
    es.indices.create(index=index_name, mappings={
      "properties": {
        "text": {
        "type": "dense_vector",
        "dims": 384,
        "similarity": "cosine",
        "index": True
        }
    }
    })
    
    ceo_res = es.index(index=index_name, id=i, body=generate_ceo())
    print(ceo_res['result'])

    cto_res = es.index(index=index_name, id=i+1, body=generate_cto())
    print(cto_res['result'])

    for j in range(0,50):
        emp_res = es.index(index=index_name, id=j+2, body=generate_employee())
        print(emp_res['result'])


index_name = "test-index" + str(datetime.now().year) + str(datetime.now().month)
res = es.get(index=index_name, id=1)
print(res['_source'])

es.indices.refresh(index=index_name)

res = es.search(index=index_name, body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])