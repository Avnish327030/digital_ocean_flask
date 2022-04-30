import logging

from app_entity.entity import DataPreprocessingEntity, DataIngestionEntity, ExperimentEntity
from app_configuration.configuration import AppConfiguration
import tensorflow as tf
from app_exception.exception import AppException
import sys
from app_entity.entity import TrainedModelEntity
from app_entity.config_entity import ModelTrainingConfig


class ModelTrainer:

    def __init__(self, data_ingestion: DataIngestionEntity,
                 data_preprocessing: DataPreprocessingEntity,
                 experiment: ExperimentEntity,
                 app_config: AppConfiguration):
        try:

            self.data_ingestion = data_ingestion
            model_training_config = app_config.get_model_training_config()
            self.trained_model = TrainedModelEntity(experiment_id=experiment.experiment_id,
                                                    model_training_config=model_training_config
                                                    )
            self.data_preprocessing = data_preprocessing
            self.trained_model.status = True
            self.trained_model.message = f"{self.trained_model.message}\nModel trainer initialized"
        except Exception as e:
            self.trained_model.status = False
            self.trained_model.message = f"{self.trained_model.message}\n{e}"
            raise AppException(e, sys) from e

    def get_model(self):
        try:
            encoder = self.data_preprocessing.encoder
            model = tf.keras.Sequential([
                encoder,
                tf.keras.layers.Embedding(len(encoder.get_vocabulary()), 64, mask_zero=True),
                tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, return_sequences=True)),
                tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
                tf.keras.layers.Dense(64, activation='relu'),
                tf.keras.layers.Dropout(0.5),
                tf.keras.layers.Dense(1)
            ])
            logging.info(model.summary())
            self.trained_model.model_architecture = model
            self.trained_model.status = True
            self.trained_model.message = f"{self.trained_model.message}\nModel architecture created."
            return model
        except Exception as e:
            self.trained_model.status = False
            self.trained_model.message = f"{self.trained_model.message}\n{e}"
            raise AppException(e, sys) from e

    def compile_model(self):
        try:
            if self.trained_model.model_architecture is None:
                self.get_model()
            self.trained_model.model_architecture.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                                                          optimizer=tf.keras.optimizers.Adam(1e-4),
                                                          metrics=['accuracy'])

            self.trained_model.is_model_compiled = True
            self.trained_model.status = True
            self.trained_model.message = f"{self.trained_model.message}\nModel compiled successfully."
        except Exception as e:
            self.trained_model.status = False
            self.trained_model.message = f"{self.trained_model.message}\n{e}"
            raise AppException(e, sys) from e

    def train_model(self):
        try:
            if not self.trained_model.is_model_compiled:
                self.compile_model()
            self.trained_model.message = f"{self.trained_model.message}\n Model training being."

            model_training_config = self.trained_model.model_training_config
            history = self.trained_model.model_architecture.fit(self.data_ingestion.train,
                                                                epochs=model_training_config.epoch,
                                                                validation_data=self.data_ingestion.test,
                                                                validation_steps=model_training_config.validation_step
                                                                )
            self.trained_model.history = history
            self.trained_model.model = self.trained_model.model_architecture
            self.trained_model.status = True
            self.trained_model.message = f"{self.trained_model.message}\nModel trained."
        except Exception as e:
            self.trained_model.status = False
            self.trained_model.message = f"{self.trained_model.message}\n{e}"
            raise AppException(e, sys) from e

    def save_model(self):
        try:
            if self.trained_model.model is None:
                self.train_model()
            model_export_dir = self.trained_model.model_training_config.model_save_dir
            message = f"Saving model in dir: [{model_export_dir}]"
            logging.info(message)
            self.trained_model.message = f"{self.trained_model.message}\n{message}"
            self.trained_model.model.save(model_export_dir)
            message = f"Model saved in dir: [{model_export_dir}]"
            logging.info(message)
            self.trained_model.message = f"{self.trained_model.message}\n{message}"
            self.trained_model.status = True
        except Exception as e:
            self.trained_model.status = False
            self.trained_model.message = f"{self.trained_model.message}\n{e}"
            raise AppException(e, sys) from e
