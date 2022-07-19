from flight_fare.entity.config_entity import DataIngestionConfig
import sys,os
from flight_fare.exception import ProjectException
from flight_fare.logger import logging
from flight_fare.entity.artifact_entity import DataIngestionArtifact
import numpy as np
from six.moves import urllib
import pandas as pd


class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise ProjectException(e,sys)

    #def download_flight_data(self,) -> str:
        
    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            #extraction remote url to download dataset
            train_download_url = self.data_ingestion_config.train_dataset_download_url
            test_download_url = self.data_ingestion_config.test_dataset_download_url
            sample_download_url = self.data_ingestion_config.sample_dataset_download_url

            if os.path.exists(self.data_ingestion_config.ingested_train_dir):
                os.remove(self.data_ingestion_config.ingested_train_dir)
            
            if os.path.exists(self.data_ingestion_config.ingested_test_dir):
                os.remove(self.data_ingestion_config.ingested_test_dir)
            
            if os.path.exists(self.data_ingestion_config.ingested_sample_dir):
                os.remove(self.data_ingestion_config.ingested_sample_dir)


            os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
            os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True)
            os.makedirs(self.data_ingestion_config.ingested_sample_dir,exist_ok=True)

            train_file_name = os.path.basename(train_download_url).split("?")[0]
            test_file_name = os.path.basename(test_download_url).split("?")[0]
            sample_file_name = os.path.basename(sample_download_url).split("?")[0]

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            train_file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        test_file_name)
                
            sample_file_path = os.path.join(self.data_ingestion_config.ingested_sample_dir,
                                        sample_file_name)
            logging.info(f"Downloading file from :[{train_download_url}] into :[{train_file_path}]")
            urllib.request.urlretrieve(train_download_url, train_file_path)
            logging.info(f"File :[{train_file_path}] has been downloaded successfully.")
            logging.info(f"Downloading file from :[{test_download_url}] into :[{test_file_path}]")
            urllib.request.urlretrieve(test_download_url, test_file_path)
            logging.info(f"File :[{test_file_path}] has been downloaded successfully.")
            logging.info(f"Downloading file from :[{sample_download_url}] into :[{sample_file_path}]")
            urllib.request.urlretrieve(sample_download_url, sample_file_path)
            logging.info(f"File :[{sample_file_path}] has been downloaded successfully.")
            
            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                    test_file_path=test_file_path,
                                    sample_file_path = sample_file_path,
                                    is_ingested=True,
                                    message=f"Data ingestion completed successfully."
                                    )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise ProjectException(e,sys) from e
    
    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            #train_file_path, test_file_path, sample_file_path =  self.download_flight_data()
            return self.split_data_as_train_test()
        
        except Exception as e:
            raise ProjectException(e,sys) from e

    def __del__(self):
        logging.info(f"{'='*20}Data Ingestion log completed.{'='*20} \n\n")