import os
from app_logger import logging
from pipeline.training_pipeline import TrainingPipeline

if __name__ == "__main__":

    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.start_training()

    except Exception as e:
        logging.error(e)
        print(e)
