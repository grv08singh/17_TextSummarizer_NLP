from textSummarizer.pipelines.s01_data_ingestion_pipeline import DataIngestionPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e