import os
from pymongo import MongoClient
from datetime import datetime

class MongoStorage:
    def __init__(self):
        host = os.environ.get('MONGO_HOST', 'mongodb')
        port = int(os.environ.get('MONGO_PORT', 27017))
        user = os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'root')
        password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD', 'root')
        db_name = os.environ.get('MONGO_DATABASE', 'pulse_raw_data')

        self.client = MongoClient(
            host=host,
            port=port,
            username=user,
            password=password,
            authSource="admin"
        )
        self.db = self.client[db_name]
        self.collection = self.db['raw_pages']

    def save_html(self, target_id, html_content):
        document = {
            "target_id": target_id,
            "content": html_content,
            "scraped_at": datetime.utcnow()
        }
        result = self.collection.insert_one(document)
        return str(result.inserted_id)

    def get_html(self, mongo_id):
        from bson.objectid import ObjectId
        doc = self.collection.find_one({"_id": ObjectId(mongo_id)})
        return doc['content'] if doc else None
