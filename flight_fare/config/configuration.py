from flight_fare.entity.config_entity import DataIngestionConfig, DataTransformationConfig,DataValidationConfig, ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig
from flight_fare.util.util import read_yaml_file
from flight_fare.logger import logging
import sys,os
from flight_fare.constant import *
from flight_fare.exception import ProjectException


class Configuartion:
    def __init__(self,
        config_file_path:str =CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP
        ) -> None:
        try:
            self.config_info  = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise ProjectException(e,sys) from e

    def get_data_ingestion_config(self) ->DataIngestionConfig:
            try:
                artifact_dir = self.training_pipeline_config.artifact_dir
                data_ingestion_artifact_dir=os.path.join(
                    artifact_dir,
                    DATA_INGESTION_ARTIFACT_DIR,
                    self.time_stamp
                )
                data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
                
                train_dataset_download_url = data_ingestion_info[DATA_INGESTION_TRAIN_DOWNLOAD_URL_KEY]
                test_dataset_download_url = data_ingestion_info[DATA_INGESTION_TEST_DOWNLOAD_URL_KEY]
                sample_dataset_download_url = data_ingestion_info[DATA_INGESTION_SAMPLE_DOWNLOAD_URL_KEY]
                
                ingested_data_dir = os.path.join(
                    data_ingestion_artifact_dir,
                    data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
                )
                ingested_train_dir = os.path.join(
                    ingested_data_dir,
                    data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
                )
                ingested_test_dir =os.path.join(
                    ingested_data_dir,
                    data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
                )
                ingested_sample_dir = os.path.join(
                    ingested_data_dir,
                    data_ingestion_info[DATA_INGESTION_SAMPLE_DIR_KEY]
                )


                data_ingestion_config=DataIngestionConfig(
                    train_dataset_download_url=train_dataset_download_url,
                    test_dataset_download_url = test_dataset_download_url,
                    sample_dataset_download_url = sample_dataset_download_url,
                    ingested_train_dir=ingested_train_dir, 
                    ingested_test_dir=ingested_test_dir,
                    ingested_sample_dir= ingested_sample_dir
                )
                logging.info(f"Data Ingestion config: {data_ingestion_config}")
                return data_ingestion_config
            except Exception as e:
                raise ProjectException(e,sys) from e

    def get_data_validation_config(self) -> DataValidationConfig:
            try:
                artifact_dir = self.training_pipeline_config.artifact_dir

                data_validation_artifact_dir=os.path.join(
                    artifact_dir,
                    DATA_VALIDATION_ARTIFACT_DIR_NAME,
                    self.time_stamp
                )
                data_validation_config = self.config_info[DATA_VALIDATION_CONFIG_KEY]


                schema_file_path = os.path.join(ROOT_DIR,
                data_validation_config[DATA_VALIDATION_SCHEMA_DIR_KEY],
                data_validation_config[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY]
                )

                report_file_path = os.path.join(data_validation_artifact_dir,
                data_validation_config[DATA_VALIDATION_REPORT_FILE_NAME_KEY]
                )

                report_page_file_path = os.path.join(data_validation_artifact_dir,
                data_validation_config[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY]

                )

                data_validation_config = DataValidationConfig(
                    schema_file_path=schema_file_path,
                    report_file_path=report_file_path,
                    report_page_file_path=report_page_file_path,
                )
                return data_validation_config
            except Exception as e:
                raise ProjectException(e,sys) from e

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self) ->ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise ProjectException(e,sys) from e