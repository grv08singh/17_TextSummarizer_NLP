import os
import urllib.request as request
from zipfile import ZipFile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
import shutil
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def get_file(self):
        if not os.path.exists(self.config.local_data_file):
            shutil.copy("notebooks/data/data.zip", self.config.local_data_file)
            logger.info(f"File copied to: {self.config.local_data_file}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file}")
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL, filename=self.config.local_data_file
            )
            logger.info(f"File downloaded successfully: {filename}")
            logger.info(f"File size: {get_size(Path(filename))}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"File extracted successfully to: {unzip_path}")