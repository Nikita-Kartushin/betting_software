import tornado.web
from stats_writer.business_models import StatsWriterStatisticsBusinessModel


class StatsWriterStatistics(tornado.web.RequestHandler):
    mongo_collection = 'user'

    async def get(self):
        """
         @api {get} /api/statistic процент дубликатов от количества общих запросов.

        :return:
        """
        result = await StatsWriterStatisticsBusinessModel().get_count_duplicates()

        self.write(str(result))

