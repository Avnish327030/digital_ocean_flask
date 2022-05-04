from collections import namedtuple
from app_entity.config_entity import DatasetConfig
from app_entity.config_entity import PreprocessingConfig, ModelTrainingConfig, TrainingPipelineConfig

from datetime import datetime


class ExperimentEntity:

    def __init__(self,
                 experiment_id=None,
                 experiment_name=None,
                 config_info=None,
                 experiment_description=None,
                 execution_start_time_stamp: datetime = None,
                 executed_by_user=None,
                 executed_by_email=None,
                 execution_stop_time_stamp: datetime = None,
                 execution_status=None,
                 execution_description=None,
                 artifacts_dir=None,
                 ):
        self.experiment_id = experiment_id
        self.experiment_name = experiment_name
        self.config_info = config_info
        self.experiment_description = experiment_description
        self.execution_start_time_stamp = execution_start_time_stamp
        self.executed_by_user = executed_by_user
        self.executed_by_email = executed_by_email
        self.execution_stop_time_stamp = execution_stop_time_stamp
        self.execution_status = execution_status
        self.execution_description = execution_description
        self.artifacts_dir = artifacts_dir


class DataIngestionEntity:
    def __init__(self, experiment_id, train, test, dataset_config: DatasetConfig):
        self.experiment_id = experiment_id,
        self.train = train
        self.test = test
        self.dataset_config = dataset_config
        self.status = None
        self.message = ""
        self.is_dataset_present = None


class DataPreprocessingEntity:
    def __init__(self, experiment_id, preprocessing_config: PreprocessingConfig):
        self.experiment_id = experiment_id,
        self.encoder = None
        self.preprocessing_config = preprocessing_config
        self.status = None
        self.message = ""


class BestModelEntity:

    def __init__(self, ):
        self.best_model = None
        self.model_path = None
        self.is_best_model_exist = None
        self.status = None
        self.message = ""


class MetricInfoEntity:

    def __init__(self,
                 train_accuracy: float = None,
                 train_loss: float = None,
                 test_accuracy: float = None,
                 test_loss: float = None
                 ):
        self.train_accuracy = train_accuracy
        self.train_loss = train_loss
        self.test_accuracy = test_accuracy
        self.test_loss = test_loss


class TrainedModelEntity:
    def __init__(self, experiment_id, model_training_config: ModelTrainingConfig):
        self.experiment_id = experiment_id
        self.model_training_config = model_training_config
        self.model_architecture = None
        self.model = None
        self.status = None
        self.message = ""
        self.is_trained_model_loaded = False
        self.is_checkpoint_model_loaded = False
        self.metric_info = MetricInfoEntity()
        self.history = None


DataValidationEntity = namedtuple("DataValidationEntity", ["experiment_id", "name"])


class ModelEvaluationEntity:
    def __init__(self, experiment_id, trained_model: TrainedModelEntity, best_model: BestModelEntity):
        self.experiment_id = experiment_id
        self.trained_model = trained_model
        self.best_model = best_model
        self.is_trained_model_accepted = False
        self.status = None
        self.message = ""


class ExportModelEntity:
    def __init__(self, experiment_id, accepted_model: TrainedModelEntity, export_dir: str):
        self.experiment_id = experiment_id
        self.accepted_model = accepted_model
        self.export_dir = export_dir
        self.status = None
        self.message = ""


class TrainingPipelineEntity:
    def __init__(self,
                 data_ingestion: DataIngestionEntity = None,
                 data_preprocessing: DataPreprocessingEntity = None,
                 model_trainer: TrainedModelEntity = None,
                 training_pipeline_config: TrainingPipelineConfig = None
                 ):
        self.model_trainer = model_trainer
        self.status = None
        self.message = ""
        self.training_pipeline_config = training_pipeline_config
        self.data_ingestion = data_ingestion
        self.data_preprocessing = data_preprocessing
