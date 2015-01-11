import tornado.web
from config.settings import conf


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    @property
    def r(self):
        return self.application.r

    @property
    def conf(self):
        return conf

    def get(self, *args, **kwargs):
        self.send_error(404)

    def get_current_user(self):
        uid = self.get_secure_cookie('uid')
        if not uid:
            return None
        else:
            self.db.user.find_one({'id': uid})

    def get_side(self):
        """获取侧边栏内容

        通用侧边栏数据
        """
        # from command.genres import get_genres
        side = {
            'genres': self.db.genres.find(),
            'nav': self.db.genres.find(),
            # 'nav': get_genres(),
        }
        return side

    def get_same_kind_movie(self, key, post):
        """获取同类影片
        genres 部分匹配，并排除自身
        """
        return self.db.movie.find({key: {'$in': post['genres']}, 'id': {'$ne': post['id']}}).limit(8)

    def get_hot_movie(self):
        """获取热门影片
        """
        return self.db.movie.find({'hot': {'$gte': conf['HOT_MOVIE']['hot']}}).limit(conf['HOT_MOVIE']['num']).\
            sort([('hot', -1)])

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('public/404.html')
        elif status_code == 500:
            self.render('public/500.html')
        else:
            self.write('error:' + str(status_code))