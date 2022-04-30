from app_logger import logging, log_function_signature
from app_entity.entity import ExperimentEntity
import uuid

class TrainingPipeline:

    def __init__(self,
                 experiment_id=None,
                 experiment_name=None,
                 experiment_description=None,
                 execution_start_time_stamp=None,
                 executed_by_user=None,
                 executed_by_email=None,
                 execution_stop_time_stamp=None,
                 execution_status=None,
                 execution_description=None,
                 artifacts_dir=None
                 ):
        ExperimentEntity(
            experiment_id=  if ex
        )
        pass

    def start_training(self):
        pass

    def get_training_status(self):
        pass
