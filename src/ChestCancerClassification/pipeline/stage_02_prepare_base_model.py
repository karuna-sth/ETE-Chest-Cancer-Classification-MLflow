from ChestCancerClassification import logger
from ChestCancerClassification.config.configuration import ConfigurationManager
from ChestCancerClassification.components.prepare_base_model import PrepareBaseModel 


STAGE_NAME = "Base Model Preparation Stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_full_model()
        

if __name__ == "__main__":
    logger.info(f"{STAGE_NAME} started.")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} Completed Successfull!")
    
    