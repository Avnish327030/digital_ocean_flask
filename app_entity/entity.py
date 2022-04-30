from collections import namedtuple

ExperimentEntity = namedtuple("ExperimentEntity", [
    "experiment_id",
    "experiment_name",
    "experiment_description",
    "execution_start_time_stamp",
    "executed_by_user",
    "executed_by_email",
    "execution_stop_time_stamp",
    "execution_status",
    "execution_description",
    "artifacts_dir",
])

DataIngestionEntity = namedtuple("DataIngestionEntity", ["experiment_id", "train", "test"])
DataValidationEntity = namedtuple("DataValidationEntity", ["experiment_id", "name"])
DataPreprocessingEntity = namedtuple("DataPreprocessingEntity", ["experiment_id", "encoder"])
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
