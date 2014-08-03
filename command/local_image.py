"""修改图片链接地址
将图片地址由豆瓣服务器切换到演示站点图片源
注意：该地址不保证永久有效

"""

from base64 import urlsafe_b64encode
from pymongo import MongoClient


client = MongoClient()
db = client.bastogne
collection = db.movie
movie = collection.find()


def convert_image(old_url):
    """地址转换
    :param old_url: 旧的地址
    :return: 新的地址
    """
    return 'http://saveimage-douban.stor.sinaapp.com/image/' + urlsafe_b64encode(old_url.encode()).decode() + '.jpg'

if __name__ == '__main__':
    for mv in movie:
        collection.update({'id': mv['id']}, {'$set': {'image': convert_image(mv['image'])}})
