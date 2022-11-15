from sensor.exception import SensorException
from sensor.logger import logging
import os,sys

def test_exception():
    try:
        logging.info("We are dividing 1 by zero")
        x = 1/0
    except Exception as e:
        raise SensorException(e,sys)
        #\ raise e

if __name__ == '__main__':
    try:
        test_exception()
    except Exception as e:
        print (e)