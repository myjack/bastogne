"""导入Elasticsearch 做全文搜索

"""


from elasticsearch import Elasticsearch
from pymongo import MongoClient

db = MongoClient().bastogne
es = Elasticsearch()


for i, movie in enumerate(db.movie.find()):
    del movie['_id']
    res = es.index(index="bastogne", doc_type='movie', id=i, body=movie)
    print(res['created'])