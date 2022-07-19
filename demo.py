from flight_fare.pipeline.pipeline import Pipeline
from flight_fare.exception import ProjectException
from flight_fare.logger import logging
from flight_fare.config.configuration import Configuartion
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #data_validation_config = Configuartion().get_data_validation_config()
        #print(data_validation_config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()