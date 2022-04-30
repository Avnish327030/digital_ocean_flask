from collections import namedtuple
from app_entity.config_entity import DatasetConfig
from app_entity.config_entity import PreprocessingConfig

ExperimentEntity = namedtuple("ExperimentEntity", [
    "experiment_id",
    "experiment_name",
    "config_info",
    "experiment_description",
    "execution_start_time_stamp",
    "executed_by_user",
    "executed_by_email",
    "execution_stop_time_stamp",
    "execution_status",
    "execution_description",
    "artifacts_dir",
])


class DataIngestionEntity:
    def __init__(self, experiment_id, train, test, dataset_config: DatasetConfig):
        self.experiment_id = experiment_id,
        self.train = train
        self.test = test
        self.dataset_config = dataset_config
        self.status = None
        self.message = ""


class DataPreprocessingEntity:
    def __init__(self, experiment_id, preprocessing_config: PreprocessingConfig):
        self.experiment_id = experiment_id,
        self.encoder = None
        self.preprocessing_config = PreprocessingConfig
        self.status = None
        self.message = ""


DataValidationEntity = namedtuple("DataValidationEntity", ["experiment_id", "name"])

BestModelEntity = namedtuple(
    "BestModelEntity", ["experiment_id", "model", "metrics", "model_path", "is_present"])

TrainedModelEntity = namedtuple("TrainedModelEntity", [
    "experiment_id", "model_architecture", "model", "metrics", "model_path", "is_present"
])

EvaluationStatusEntity = namedtuple("EvaluationStatusEntity", [
    "experiment_id",
    "best_model",
    "is_updated",
    "metrics",
    "is_accepted",
    "evaluated_timestamp"])

ModelDeploymentEntity = namedtuple("ModelDeploymentEntity", ["experiment_id",
                                                             "deployment_id", "deployment_name",
                                                             "deployment_description",
                                                             "deployment_start_time_stamp",
                                                             "deployment_stop_time_stamp",
                                                             "deployment_status", "deployment_artifacts_dir"])
