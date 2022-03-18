from database import mongo_session


class StatsWriterStatisticsBusinessModel:
    mongo_collection = 'user'

    async def get_count_duplicates(self):
        betting_software_collection = mongo_session()[self.mongo_collection]
        motor_cursor = betting_software_collection.aggregate([{"$sortByCount": "$key"}])

        duplicates_count = 0
        count = await betting_software_collection.count_documents({})

        async for doc in motor_cursor:
            duplicates_count += doc.get('count') - 1

        if count == 0:
            return 0

        result = duplicates_count / count * 100

        return result
