import os
import sys
from source_code.logger import logging
from source_code.exception import CustomException
import pandas as pd

from source_code.components.data_ingestion import DataIngestion

if __name__=="main":
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)