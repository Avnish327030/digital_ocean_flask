from collections import namedtuple
from app_logger import logging,log_function_signature

from app_exception import AppException
import sys

class ModelEvaluation:

    def __init__(self,model,test_dataset):
        try:
            pass
        except Exception as e:
            raise AppException(e,sys) from e


    def get_best_model(self):
        try:
            pass
        except Exception as e:
            raise AppException(e,sys) from e
        return self.best_model

    def get_trained_model(self):
        try:
            pass
        except Exception as e:
            raise AppException(e,sys) from e
        return self.trained_model

