import json
from urllib.request import urlopen
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import torch


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
                "title_vector": {
                    "type": "dense_vector",
                    "dims": 384,
                    "index": "true",
                    "similarity": "cosine"
                }
            }
        }

        if not self.es.indices.exists(index='book_index'):
            # Create the index
            self.es.indices.create(index='book_index', mappings=mapping)
            url = "https://raw.githubusercontent.com/elastic/elasticsearch-labs/main/notebooks/search/data.json"
            response = urlopen(url)
            books = json.loads(response.read())

            actions = []
            for book in books:
                actions.append({"index": {"_index": "book_index"}})
                # Transforming the title into an embedding using the model
                book["title_vector"] = self.model.encode(book["title"]).tolist()
                actions.append(book)
            self.es.bulk(index="book_index", operations=actions)


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
        response = self.es.knn_search(index="book_index", knn={
            "field": "title_vector",
            "query_vector": self.model.encode("Best javascript books?"),
            "k": 10,
            "num_candidates": 100
        })
        # print(response)
        self.pretty_response(response)


def main():
    bookSearch = BookSearch()
    bookSearch.insert_data()
    bookSearch.semantic_search()

if __name__ == '__main__':
    main()