from utils import redis_mongo
KEY_REDIS_EXPIRED = "__keyevent@0__:expired"
KEY_REDIS_SET = "__keyevent@0__:set"
KEY_REDIS_EXPIRE = '__keyevent@0__:expire'
KEY_CHANNEL = 'channel'
KEY_DATA = 'data'


class Listener(redis_mongo.StrictRedisMongo):
    def __init__(self, **kwargs):
        redis_mongo.StrictRedisMongo.__init__(self, **kwargs)
        self.pubsub = self.pubsub()
        self.pubsub.psubscribe(kwargs.get('sub', "*"))
        self.logger = kwargs.get('logger', None)

    def listen(self):
        for message in self.pubsub.listen():
            if self.logger:
                self.logger.debug(message)
            self.save_action(message=message)

    def save_action(self, message):
        if KEY_REDIS_EXPIRE == message[KEY_CHANNEL]:
            if self.logger:
                self.logger.debug("KEY_REDIS_EXPIRE begin to save")
            data = {message[KEY_DATA]: self.get(message[KEY_DATA])}
            self.save(data=data)
            if self.db.find_one(data) is not None:
                if self.logger:
                    self.logger.info("data save")
                    self.logger.debug(data)
            else:
                if self.logger:
                    self.logger.error("please make sur your data is saved")

