from ChestCancerClassification import logger
from ChestCancerClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f"{STAGE_NAME} started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e