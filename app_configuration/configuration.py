from select import select
import yaml
import os,sys
from app_exception.exception import AppException
from app_utils.util import read_yaml_file
from collections import namedtuple
from app_logger import logging,log_function_signature
#Initializing the default values for app configuration
CONFIG_FILE_DIR = os.getcwd()
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(CONFIG_FILE_DIR, CONFIG_FILE_NAME)


#dataset keys   
DATA_SET_KEY = "data_set"
DATA_SET_NAME_KEY = "name"

DatasetConfig = namedtuple("DatasetConfig", ["name"])
#preprocessing keys

PREPROCESSING_KEY = "preprocessing"
VOCAB_SIZE_KEY = "vocab_size"


#training configuration keys
TRAINING_KEY = "train_config"
BUFFER_SIZE_KEY = "buffer_size"
BATCH_SIZE_KEY = "batch_size"




class AppConfiguration:
    """
    Reads the configuration file and returns the configuration object
    """
    @log_function_signature
    def __init__(self):
        try:
            self.logger=logging
            self.logger.info("Reading the configuration file.")
            self.config_info = read_yaml_file(config_file_path=CONFIG_FILE_PATH)
            self.logger.info("Configuration file read successfully.")
        except Exception as e:
            raise AppException(e,sys) from e

    @log_function_signature
    def get_dataset_configuration(self)->DatasetConfig:
        try:
            dataset_config = self.config_info[DATA_SET_KEY]
            self.logger.info(f"Dataset configuration :\n{dataset_config}\n read successfully.")
            response = DatasetConfig(name=dataset_config[DATA_SET_NAME_KEY])
            return response
        except Exception as e:
            raise AppException(e,sys) from e

    def __repr__(self) -> str:
        return f"AppConfiguration()"

    def __str__(self) -> str:
        return f"AppConfiguration()"


        
