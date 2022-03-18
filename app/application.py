import tornado.web
from stats_writer import routes


def create_app():
    app = tornado.web.Application(routes)

    return app
