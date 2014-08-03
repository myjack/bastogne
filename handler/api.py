"""简单的电影信息api
"""
import json
from .base import BaseHandler


def result(flag=False, data=None):
    """定义数据返回格式"""
    return {
        'res': flag,
        'data': data
    }


class MovieHandler(BaseHandler):
    """根据电影名获取电影信息"""
    def get(self):
        title = self.get_argument('title', '')
        post = self.db.movie.find_one({'title': title}, {'_id': 0})
        if post:
            #http://www.tornadoweb.org/en/stable/_modules/tornado/web.html#RequestHandler.write
            self.write(result(True, post))
        else:
            self.write(result(False))


class MovieKeyWordHandler(BaseHandler):
    """根据关键词获取电影信息"""
    def get(self):
        key = self.get_argument('key', '')
        res = list(map(lambda x: x.decode(), self.r.sdiff(key)))
        self.write(result(True, res))
