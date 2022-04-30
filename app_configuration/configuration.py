from select import select
import yaml
import os, sys
from app_exception.exception import AppException
from app_utils.util import read_yaml_file
from collections import namedtuple
from app_logger import logging, log_function_signature
from app_entity.config_entity import DatasetConfig, PreprocessingConfig

# Initializing the default values for app configuration

ROOT_DIR = os.getcwd()
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_FILE_NAME)

SCHEMA_FILE_NAME = "dataset_schema.yaml"
SCHEMA_FILE_PATH = os.path.join(ROOT_DIR, SCHEMA_FILE_NAME)

# dataset keys
DATA_SET_KEY = "data_set"
DATA_SET_NAME_KEY = "name"
SCHEMA_KEY = "schema"


# preprocessing keys

PREPROCESSING_KEY = "preprocessing"
VOCAB_SIZE_KEY = "vocab_size"

# training configuration keys
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
            self.logger = logging
            self.logger.info("Reading the configuration file.")
            self.config_info = read_yaml_file(yaml_file_path=CONFIG_FILE_PATH)
            self.dataset_schema = read_yaml_file(yaml_file_path=SCHEMA_FILE_PATH)
            self.logger.info("Configuration file read successfully.")
        except Exception as e:
            raise AppException(e, sys) from e

    @log_function_signature
    def get_dataset_configuration(self) -> DatasetConfig:
        try:
            dataset_config = self.config_info[DATA_SET_KEY]
            self.logger.info(f"Dataset configuration :\n{dataset_config}\n read successfully.")
            response = DatasetConfig(name=dataset_config[DATA_SET_NAME_KEY],
                                     schema=self.dataset_schema[SCHEMA_KEY],
                                     )
            return response
        except Exception as e:
            raise AppException(e, sys) from e

    @log_function_signature
    def get_preprocessing_configuration(self) -> PreprocessingConfig:
        try:
            preprocessing_config = self.config_info[PREPROCESSING_KEY]
            self.logger.info(f"Preprocessing configuration :\n{preprocessing_config}\n read successfully.")
            response = PreprocessingConfig(vocal_size=preprocessing_config[VOCAB_SIZE_KEY])
            return response
        except Exception as e:
            raise AppException(e, sys) from e

    def __repr__(self) -> str:
        return f"AppConfiguration()"

    def __str__(self) -> str:
        return f"AppConfiguration()"
