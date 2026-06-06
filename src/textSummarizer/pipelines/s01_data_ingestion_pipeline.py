from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger
import os


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)

            #if local_data_file doesn't exist in artifacts directory
            if not os.path.exists(data_ingestion.config.local_data_file):
                #if file exists at notebooks/data/data.zip, copy the file
                if os.path.exists("notebooks/data/data.zip"):
                    data_ingestion.get_file()
                #else download the file
                else:
                    data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e