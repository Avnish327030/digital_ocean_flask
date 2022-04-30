# configuration entity
from collections import namedtuple

DatasetConfig = namedtuple("DatasetConfig", ["name", "schema", "buffer_size","batch_size"])
PreprocessingConfig = namedtuple("PreprocessingConfig", ["vocal_size"])
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",)
