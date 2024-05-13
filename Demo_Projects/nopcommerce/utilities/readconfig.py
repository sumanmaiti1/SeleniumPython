import os
from configparser import ConfigParser
from configparser import NoOptionError,NoSectionError,DuplicateOptionError,DuplicateSectionError
# from nopcommerce.configuration.configuration import config_file_path
from nopcommerce.utilities.loggen import LogGen

class ReadConfig:
    """This Class will read configurations from config file"""

    @staticmethod
    def read_config(strsection,stroption):
        try:
            __config = ConfigParser()
            __config_file_path = os.path.abspath(os.path.dirname(__file__) + '/..' + "\\configuration\\config.ini")
            __config.read(__config_file_path)
            return __config.get(strsection,stroption)
        except (NoOptionError,NoSectionError) as err:
            LogGen.log_gen().error(f'Runtime exception {type(err).__name__} is generated. Error:{err}')
        except (DuplicateOptionError,DuplicateSectionError) as err:
            LogGen.log_gen().error(f'Runtime exception {type(err).__name__} is generated. Error:{err}')
        except Exception as err:
            LogGen.log_gen().error(f'Runtime exception {type(err).__name__} is generated from base exception. Error:{err}')
