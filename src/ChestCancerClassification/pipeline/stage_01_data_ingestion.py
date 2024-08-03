from ChestCancerClassification import logger
from ChestCancerClassification.components.data_ingestion import DataIngestion
from ChestCancerClassification.config.configuration import ConfigurationManager


STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingesion = DataIngestion(config=data_ingestion_config)
            data_ingesion.download_file()
            data_ingesion.extract_file()
        except Exception as ex:
            raise ex
        

if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise