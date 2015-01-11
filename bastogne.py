import redis
from pymongo import MongoClient
import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.options
from tornado.options import define, options
from config.settings import settings, redis as redis_conf
from config.urls import urls as handlers
from uimodules import uimodules


define('port', default=8000, help='监听端口', type=int)
settings['ui_modules'] = uimodules
handlers.append((r"(apple-touch-icon\.png)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])))


class Application(tornado.web.Application):
    def __init__(self):
        client = MongoClient()
        self.db = client.bastogne
        self.r = redis.StrictRedis(**redis_conf)

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
