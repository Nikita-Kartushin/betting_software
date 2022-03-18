from utils import logger
from utils import redirect_logs
from tornado.ioloop import IOLoop
from application import create_app
from tornado.httpserver import HTTPServer


@redirect_logs
def main():
    # Create application
    app = create_app()

    # Configuration server
    server = HTTPServer(app)
    server.listen(8000)

    # Start IOLoop
    IOLoop.current().start()


if __name__ == '__main__':
    main(logger)
