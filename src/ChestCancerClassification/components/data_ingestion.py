import os
import zipfile
import gdown
from ChestCancerClassification import logger
from ChestCancerClassification.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config
        
    def download_file(self) -> str:
        try:
            dataset_url = self.config.source_URL
            zip_download_url = self.config.local_data_file
            os.makedirs(self.config.root_dir, exist_ok=True)
            
            logger.info(f"Downloading dataset into {zip_download_url}")
            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id, zip_download_url)
            
            logger.info("Download completed.")
        except Exception as ex:
            raise ex
    
    
    def extract_file(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            
            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)
            
            logger.info("File Extraction completed.")
            
        except Exception as ex:
            raise ex