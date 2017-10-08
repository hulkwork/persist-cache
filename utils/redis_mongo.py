import redis
from pymongo import MongoClient


class StrictRedisMongo(redis.StrictRedis):
    def __init__(self, **kwargs):

        self.conf_mongo = kwargs.get("conf_mongo", None)
        redis.StrictRedis.__init__(self)
        # TODO : put credential if you need
        if self.conf_mongo is not None:
            self.client_mongo = MongoClient(host=self.conf_mongo['host'], port=self.conf_mongo['port'])
            if "collection_name" in self.conf_mongo:
                self.collection_name = self.conf_mongo["collection_name"]
                self.collection = self.client_mongo[self.collection_name]
            if 'db_name' in self.conf_mongo:
                self.db_name = self.conf_mongo["db_name"]
                self.db = self.collection[self.db_name]

    def save(self, data):
        if self.conf_mongo is None:
            redis.StrictRedis.save(self)
        else:
            self.db.insert_one(data)
