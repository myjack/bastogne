import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import jieba
from pymongo import MongoClient
import redis
from config.settings import redis as redis_conf


r = redis.StrictRedis(**redis_conf)


client = MongoClient()
db = client.bastogne
movie = db.movie


def add_all():
    for m in movie.find():
        results = jieba.cut_for_search(m['title'])
        for res in results:
            json_data = dict()
            json_data["id"] = m["id"]
            json_data["title"] = m["title"]
            json_data["image"] = m["image"]
            r.sadd(res, json.dumps(json_data))


if __name__ == '__main__':
    add_all()
    data = r.smembers('正传')
    for d in data:
        print(d.decode())


