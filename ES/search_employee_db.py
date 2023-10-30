from datetime import datetime
import json
from urllib.request import urlopen
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import torch
from random_employee import generate_ceo
from random_employee import generate_cto
from random_employee import generate_employee


class Book:
    def __init__(self, title, summary, publish_date, publisher, num_reviews, authors):
        self.title = title
        self.summary = summary
        self.publish_date = publish_date
        self.publisher = publisher
        self.num_reviews = num_reviews
        self.authors = authors

class BookSearch:
    es : Elasticsearch
    model : SentenceTransformer

    def __init__(self):
        self.es = Elasticsearch(
            ['http://localhost:9200'],
            # no verify SSL certificates
            verify_certs=False,
            # don't show warnings about ssl certs verification
            ssl_show_warn=False
        )
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = SentenceTransformer('all-MiniLM-L6-v2', device=device)
    
    def insert_data(self):
        # Define the mapping
        mapping = {
            "properties": {
                "employee_vector": {
                    "type": "dense_vector",
                    "dims": 384,
                    "index": "true",
                    "similarity": "cosine"
                }
            }
        }

        for i in range(0,6):
            index_name = "test-index-" + str(datetime.now().year) + str(datetime.now().month-i)
            print('=========>', index_name)
            if not self.es.indices.exists(index=index_name):
                self.es.indices.create(index=index_name, mappings=mapping)
        
                ceo_res = self.es.index(index=index_name, id=i, body=generate_ceo())
                print(ceo_res['result'])

                cto_res = self.es.index(index=index_name, id=i+1, body=generate_cto())
                print(cto_res['result'])

                for j in range(0,50):
                    emp_res = self.es.index(index=index_name, id=j+2, body=generate_employee())
                    print(emp_res['result'])        


    def pretty_response(self, response):
        for hit in response['hits']['hits']:
            id = hit['_id']
            publication_date = hit['_source']['publish_date']
            score = hit['_score']
            title = hit['_source']['title']
            summary = hit['_source']['summary']
            publisher = hit["_source"]["publisher"]
            num_reviews = hit["_source"]["num_reviews"]
            authors = hit["_source"]["authors"]
            pretty_output = (f"\nID: {id}\nPublication date: {publication_date}\nTitle: {title}\nSummary: {summary}\nPublisher: {publisher}\nReviews: {num_reviews}\nAuthors: {authors}\nScore: {score}")
            print(pretty_output)


    def semantic_search(self):
        response = self.es.search(index="test-index-20238", knn={
            "field": "employee_vector",
            "query_vector": self.model.encode("How many designations are there?"),
            "k": 10,
            "num_candidates": 100
        })
        print(response)
        self.pretty_response(response)

    def semantic_search_filter(self):
        response = self.es.search(index="test-index-20238", knn={
            "field": "employee_vector",
            "query_vector": self.model.encode("What is the role of a CEO?"),
            "k": 10,
            "num_candidates": 100,
            "filter": {
               "term": {
                  "publisher": "addison-wesley"
                }
            }
        })
        # print(response)
        self.pretty_response(response)


    def semantic_search_adv_filters(self):
        response = self.es.search(index="test-index-20238", knn={
            "field": "title_vector",
            "query_vector": self.model.encode("What is the role of a CEO?"),
            "k": 10,
            "num_candidates": 100,
            "filter": {
                "bool": {
                    "should": [
                        {
                            "term": {
                                "publisher": "addison-wesley"
                            }
                        },
                        {
                            "term": {
                                "authors": "robert c. martin"
                            }
                        }
                    ],

                }
            }
        })
        # print(response)
        self.pretty_response(response)

    def semantic_hybrid_search(self):
        response = self.es.search(index="book_index", query={
            "query": {
                "match": {
                    "summary": "python"
                }
            },
            "knn": {
                "field": "title_vector",
                # generate embedding for query so it can be compared to `title_vector`
                "query_vector" : self.model.encode("python programming").tolist(),
                "k": 5,
                "num_candidates": 10
            },
            "rank": {
                "rrf": {
                    "window_size": 100,
                    "rank_constant": 20
                }
            }
        })
        # print(response)
        self.pretty_response(response)



def main():
    bookSearch = BookSearch()
    bookSearch.insert_data()
    print('====================')
    bookSearch.semantic_search()
    # print('====================')
    # bookSearch.semantic_search_filter()
    # print('====================')
    # bookSearch.semantic_search_adv_filters()
    # print('====================')
    # bookSearch.semantic_hybrid_search()

if __name__ == '__main__':
    main()