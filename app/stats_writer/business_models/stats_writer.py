from database import mongo_session
from utils import generate_key_from_dict


class StatsWriterBusinessModel:
    mongo_collection = 'user'

    async def add_body_request(self, body_request: dict):
        key = generate_key_from_dict(body_request)

        body_request_model = {
            'key': key,
            'body': body_request
        }

        betting_software_collection = mongo_session()[self.mongo_collection]
        await betting_software_collection.insert_one(body_request_model)
        return key

    async def get_body_request(self, key: str):
        betting_software_collection = mongo_session()[self.mongo_collection]
        body_request_model = await betting_software_collection.find_one({'key': key})
        return body_request_model

    async def delete_bode_request(self, key: str):
        betting_software_collection = mongo_session()[self.mongo_collection]
        await betting_software_collection.delete_one({'key': key})
