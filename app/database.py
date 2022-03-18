from configs import config
from motor.motor_asyncio import AsyncIOMotorClient


class MongoSession:
    session = None

    def __init__(self, host=None, port=None, database=None, username=None, password=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    def __call__(self):
        credentials = f'{self.username}:{self.password}@' if self.username else ''
        auth_str = f'mongodb://{credentials}{self.host}:{self.port}/{self.database}'
        client = AsyncIOMotorClient(auth_str)
        client = client[self.database]

        if not MongoSession.session:
            MongoSession.session = client
        return MongoSession.session


mongo_session = MongoSession(**config['mongo'])
