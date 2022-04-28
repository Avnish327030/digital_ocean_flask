from app_exception.exception import AppException
from app_configuration.configuration import AppConfiguration
from app_logger.logger import logging,log_function_signature
import os,sys
import tensorflow_datasets as tfds
from collections import namedtuple
import tensorflow as tf
TRAIN_KEY = "train"
TEST_KEY = "test"

Dataset = namedtuple("Dataset",["train","test","dataset_info"])
class DataLoader:

    @log_function_signature
    def __init__(self):
        try:
            self.logger=logging
            self.logger.info("Reading the dataset configuration.")
            self.data_set_config = AppConfiguration().get_dataset_configuration()
            self.logger.info(f"Dataset configuration :\n{self.data_set_config}\n read successfully")
            self.train_dataset=None
            self.test_dataset=None
            self.dataset_info=None     
        except Exception as e:
            raise AppException(e,sys) from e


    @log_function_signature
    def get_dataset(self)->Dataset:
        try:
            self.logger.info("Reading the dataset")
            print(self.data_set_config)
            dataset, self.dataset_info = tfds.load(self.data_set_config.name, with_info=True,
                          as_supervised=True)
            self.train_dataset, self.test_dataset = dataset[TRAIN_KEY], dataset[TEST_KEY]
            self.logger.info("Dataset read successfully")
            return Dataset(self.train_dataset,self.test_dataset,self.dataset_info)
        except Exception as e:
            raise AppException(e,sys) from e

    @log_function_signature
    def get_batch_suffle_datset(self,buffer_size,batch_size):
        try:
            self.logger.info(f"{self.get_batch_suffle_datset.__name__}(self,{buffer_size},{batch_size})")
            self.train_dataset = self.train_dataset.shuffle(buffer_size).batch(batch_size).prefetch(tf.data.AUTOTUNE)
            self.test_dataset = self.test_dataset.batch(batch_size).prefetch(tf.data.AUTOTUNE)
            self.logger.info("Dataset shuffled and batched successfully")
            return Dataset(self.train_dataset,self.test_dataset,self.dataset_info)
        except Exception as e:
            raise AppException(e,sys) from e

    
    def __repr__(self):
        return f"DataLoader()"

    def __str__(self):
        return f"DataLoader()"