from .controllers import *

routes = [
    (r'/api/add', StatsWriterController),
    (r'/api/get', StatsWriterController),
    (r'/api/remove', StatsWriterController),
    (r'/api/update', StatsWriterController),
    (r'/api/statistic', StatsWriterStatistics)
]
