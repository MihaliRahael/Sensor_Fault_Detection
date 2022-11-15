import os
import sys
import certifi
import pymongo

from sensor.constant.database import DATABASE_NAME 
#from sensor.constant.env_variable import MONGODB_URL_KEY
#from sensor.exception import SensorException

ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                #mongo_db_url = os.getenv(MONGODB_URL_KEY)
                mongo_db_url = "mongodb+srv://iNeuron:RsPGmJUa69n558n@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"
                #mongo_db_url = "mongodb+srv://Bonny:Mihali2342@cluster0.3uxym7b.mongodb.net/?retryWrites=true&w=majority"
                '''
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                '''
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client

            self.database = self.client[database_name]

            self.database_name = database_name

        except Exception as e:
            #raise SensorException(e, sys)
            raise e