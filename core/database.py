from conf.configparser import conf
from pymongo import MongoClient

class Database:
    """Interact with conf variables."""

    be_session = MongoClient(host=conf['mongo']['host'],
                             port=int(conf['mongo']['port'])).get_database('betexplorer')

    @classmethod
    def get_session_sportmonks(cls):
        return cls.sm_session

    @classmethod
    def get_session_betfair(cls):
        return cls.bf_session

    @classmethod
    def get_session_betexplorer(cls):
        return cls.be_session

    @classmethod
    def open_new_session_betexplorer(cls):
        return MongoClient(host=conf['mongo']['host'],
                           port=int(conf['mongo']['port'])).get_database('betexplorer')