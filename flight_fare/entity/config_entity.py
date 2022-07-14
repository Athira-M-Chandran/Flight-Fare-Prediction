from collections import namedtuple


DataIngestionConfig=namedtuple("DataIngestionConfig",
[
    "train_dataset_download_url",
    "test_dataset_download_url",
    "sample_dataset_download_url",
    "ingested_train_dir",
    "ingested_test_dir",
    "ingested_sample_dir"
    ])


DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path",
                                                            "report_file_path",
                                                            "report_page_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig", ["Journey_date",
                                                                "Journey_month",
                                                                "Dep_hour","Dep_min",
                                                                "Arrival_hour", "Arrival_min",
                                                                "transformed_train_dir",
                                                                "transformed_test_dir",
                                                                "preprocessed_object_file_path"])


ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path","base_accuracy","model_config_file_path"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])