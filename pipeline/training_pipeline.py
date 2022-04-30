from app_logger import logging, log_function_signature
from app_entity.entity import ExperimentEntity
import uuid
from datetime import datetime
from app_configuration.configuration import  AppConfiguration

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

        app_config = AppConfiguration()
        self.experiment = ExperimentEntity(
            experiment_id=str(uuid.uuid4()) if experiment_id is None else experiment_id,
            experiment_name=experiment_name,
            config_info=app_config.config_info,
            experiment_description=experiment_description,
            execution_start_time_stamp=datetime.now(),
            executed_by_user=executed_by_user,
            executed_by_email=executed_by_email,
            execution_stop_time_stamp=execution_stop_time_stamp,
            execution_status=execution_status,
            execution_description=execution_description,
            artifacts_dir=artifacts_dir
        )




    def start_training(self):
        pass

    def get_training_status(self):
        pass


if __name__=="__main__":
    training_pipeline = TrainingPipeline()
    training_pipeline.start_training()