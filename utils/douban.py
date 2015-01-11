"""豆瓣电影
"""

import json
from urllib.request import urlopen
from urllib.error import HTTPError


class Movie():
    url = 'https://api.douban.com/v2/movie/'

    def __init__(self):
        pass

    def get_subject_by_id(self, movie_id):
        """根据豆瓣电影id获取豆瓣电影条目

        :param movie_id: 豆瓣电影id
        :return: 电影条目信息
        """
        url = self.url + 'subject/' + str(movie_id)
        response = urlopen(url)
        return json.loads(response.read().decode())

    def convert(self, movie):
        """转换为bastogne影片格式

        :param movie: 豆瓣电影条目
        :return: Bastogne格式电影条目
        """
        mv = dict()
        mv['alt'] = movie['alt']
        mv['rating'] = movie['rating']['average']
        mv['image'] = movie['images']['large']
        mv['year'] = movie['year']
        mv['countries'] = movie['countries']
        mv['genres'] = movie['genres']

        mv['directors'] = []

        for director in movie['directors']:
            mv['directors'].append(director['name'])

        mv['casts'] = []

        for cast in movie['casts']:
            mv['casts'].append(cast['name'])

        mv['summary'] = movie['summary']
        mv['download'] = []

        return mv

    def get(self, movie_id):
        return self.convert(self.get_subject_by_id(movie_id))


if __name__ == '__main__':
    movie = Movie()
    print(movie.get(1292052))