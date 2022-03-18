import json
import tornado.web
from utils import logger
from stats_writer.business_models import StatsWriterBusinessModel


class StatsWriterController(tornado.web.RequestHandler):
    async def get(self):
        """
        @api {get} /api/get?key=key Возвращает тело запроса по ключу
        @apiQueryParams
            key - ключ, по которому можно вернуть тело запроса

        :return:
        """
        key = self.get_query_argument('key')
        logger.info(f'Incoming request get. Get body_request for key {key}')

        stats_writer_business_model = StatsWriterBusinessModel()
        body_request = await stats_writer_business_model.get_body_request(key=key)

        self.write(str(body_request))

    async def post(self):
        """
        @api {post} /api/add Добавление в БД тела запроса
        @apiDescription Возвращает ключ, по которому можно получить тело запроса

        @apiExample Request-Example
            {
                ...
            }

        :return:
        """
        body = json.loads(self.request.body)
        logger.info(f'Incoming request post. Add body_request')

        stats_writer_business_model = StatsWriterBusinessModel()
        key = await stats_writer_business_model.add_body_request(body)
        self.write(key)

    async def delete(self):
        """
        @api {post} /api/remove?key=key Удаление записи из БД по ключу
        @apiQueryParams
            key - ключ, по которому можно вернуть тело запроса

        :return:
        """
        key = self.get_query_argument('key')
        logger.info(f'Incoming request delete. Get body_request for key {key}')

        stats_writer_business_model = StatsWriterBusinessModel()
        await stats_writer_business_model.delete_bode_request(key=key)
        self.write('Body request was deleted!')

    async def put(self):
        """
        @api {put} /api/update?key=key Изменение записи в БД по ключу
        @apiQueryParams
            key - ключ, по которому изменяется тело запроса

        :return:
        """
        key = self.get_query_argument('key')
        body = json.loads(self.request.body)
        logger.info(f'Incoming request update. Get body_request for key {key}')

        stats_writer_business_model = StatsWriterBusinessModel()
        new_key = await stats_writer_business_model.update_body_request(key=key, body_request=body)

        self.write(new_key)

