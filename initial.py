from src.stage_00_data_loader import DataLoader
from app_logger import logging,log_function_signature
from app_exception import AppException
import sys


def main():
    try:
        data_loader = DataLoader()
        data_loader.get_dataset()
        data_loader.get_batch_suffle_datset(buffer_size=100,batch_size=32,ashbdjas=326472) 
    except Exception as e:
        e=AppException(e,sys)
        logging.debug(e)
        print(e)


if __name__ == '__main__':
    main() 