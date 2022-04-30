from app_exception.exception import AppException
from app_configuration.configuration import AppConfiguration
from app_logger.logger import logging
import os,sys
import tensorflow_datasets as tfds
from collections import namedtuple
import tensorflow as tf
f
class DataPreprocessing:


    def __init__(self):
        try:
            self.logger=logging
            self.logger.info("Reading the dataset configuration.")
            self.preprocessing_config = AppConfiguration().get_preprocessing_configuration()
            self.logger.info(f"Dataset configuration :\n{self.data_set_config}\n read successfully")
            self.train_dataset=None
            self.test_dataset=None
            self.dataset_info=None     
        except Exception as e:
            raise AppException(e,sys) from e

    def get_text_encoder(self):
        try:
            self.logger.info("Creating the text encoder.")
            self.text_encoder = tfds.features.text.SubwordTextEncoder.build_from_corpus(
                self.train_dataset['text'], target_vocab_size=self.preprocessing_config.vocal_size)
            self.logger.info("Text encoder created successfully.")
        except Exception as e:
            raise AppException(e,sys) from e


    