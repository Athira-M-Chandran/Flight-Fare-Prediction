from collections import namedtuple
from datetime import datetime
import uuid
from threading import Thread
from typing import List
from multiprocessing import Process
import os, sys
from collections import namedtuple
from datetime import datetime
import pandas as pd

from flight_fare.logger import logging, get_log_file_name
from flight_fare.exception import ProjectException
from flight_fare.config.configuration import Configuartion
from flight_fare.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from flight_fare.entity.config_entity import DataIngestionConfig, ModelEvaluationConfig
from flight_fare.component.data_ingestion import DataIngestion
from flight_fare.component.data_validation import DataValidation
from flight_fare.constant import EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME

class Pipeline:

    def __init__(self,config: Configuartion = Configuartion()) -> None:
        try:
            self.config=config

        except Exception as e:
            raise ProjectException(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise ProjectException(e,sys) from e  

    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)-> DataValidationArtifact :
        try:
            data_validation =  DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                              data_ingestion_artifact=data_ingestion_artifact
            )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise ProjectException(e,sys) from e

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass

    def run_pipeline(self):
        try:
            #data ingestion

            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)

            


        except Exception as e:
            raise ProjectException(e,sys) from e