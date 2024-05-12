import logging
import inspect
import os
from nopcommerce.configuration import configuration as config


class LogGen:
    """This class will be responsible to generate execution log"""

    if not os.path.exists(config.report_path):
        os.mkdir(config.report_path)
    __log_path = config.report_path + "\execution_log.log"
    __logger_formatter = logging.Formatter('%(asctime)8s - %(name)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s', datefmt='[%d-%b-%y %H:%M:%S]')
    __logger_handler = logging.FileHandler(filename=__log_path, mode='w')
    __logger_handler.setFormatter(__logger_formatter)

    @staticmethod
    def log_gen():
        """This method will log execution logs in log file"""
        __logger = logging.getLogger('NopCommerce - ' + inspect.stack()[1][3])
        __logger.setLevel(logging.INFO)
        __logger.addHandler(LogGen.__logger_handler)
        return __logger
