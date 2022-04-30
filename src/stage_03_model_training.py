
from app_entity.entity import DataPreprocessingEntity,DataIngestionEntity,ExperimentEntity
from app_configuration.configuration import AppConfiguration
import tensorflow as tf
from app_exception.exception import  AppException
import sys

class ModelTrainer:

    def __init__(self, data_ingestion: DataIngestionEntity,
                 experiment: ExperimentEntity,
                 app_config: AppConfiguration):
        try:
            pass

        except Exception as e:
            raise  AppException(e,sys) from e

    def get_model(self,encoder):
        model = tf.keras.Sequential([
                encoder,
                tf.keras.layers.Embedding(len(encoder.get_vocabulary()), 64, mask_zero=True),
                tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64,  return_sequences=True)),
                tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
                tf.keras.layers.Dense(64, activation='relu'),
                tf.keras.layers.Dropout(0.5),
                tf.keras.layers.Dense(1)    
                ])
        return model

        
