import yaml
import os, sys
from app_exception.exception import AppException
from app_logger.logger import logging, log_function_signature
import json
from copy import deepcopy


@log_function_signature
def read_json_file(file_path: str) -> dict:
    try:
        response = dict()
        if os.path.exists(file_path):
            try:
                with open(file_path) as json_file:
                    response.update(dict(json.load(json_file)))
            except Exception as e:
                logging.info(e)
                pass

        return dict(response)
    except Exception as e:
        raise AppException(e, sys) from e


@log_function_signature
def write_json_file(obj: dict, file_path: str):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        response = dict()
        existing_content = dict()
        if os.path.exists(file_path):
            existing_content = read_json_file(file_path=file_path)

        response = deepcopy(existing_content)
        response.update(obj)
        try:
            with open(file_path, "w") as json_file:
                json.dump(response, json_file, indent=6)
        except Exception as e:
            with open(file_path, "w") as json_file:
                json.dump(existing_content, json_file, indent=6)


    except Exception as e:
        raise AppException(e, sys) from e


def read_yaml_file(yaml_file_path: str) -> dict:
    try:
        logging.info("Reading the configuration file")
        with open(yaml_file_path, "rb") as config_file:
            config_dict = yaml.safe_load(config_file)
            logging.info("Configuration file read successfully")
            return config_dict
    except Exception as e:
        raise AppException(e, sys) from e
