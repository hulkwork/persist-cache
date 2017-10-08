from utils import redis_mongo
from datetime import datetime
from utils import listener as Listener
from utils import daemon
import logging
import pickle
import conf
import os

basedir = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(basedir,"../",conf.LOG_PATH)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(log_path)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Persitency(daemon.Daemon):
    def __init__(self,pidfile,logger):
        daemon.Daemon.__init__(self,pidfile=pidfile,logger=logger)
        self.lister = Listener.Listener(host=conf.CONFIG_REDIS["host"], port=conf.CONFIG_REDIS["port"],
                                   conf_mongo=conf.CONFIG_MONGO, logger=logger)

    def run(self):
        logger.info("You deamon is start")
        self.lister.listen()
