# configuration entity
from collections import namedtuple

DatasetConfig = namedtuple("DatasetConfig", ["name", "schema", ])
PreprocessingConfig = namedtuple("PreprocessingConfig", ["vocal_size"])
