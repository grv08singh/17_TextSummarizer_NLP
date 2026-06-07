import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from textSummarizer.pipelines.s01_data_ingestion_pipeline import DataIngestionPipeline
from textSummarizer.pipelines.s02_data_validation_pipeline import DataValidationPipeline
from textSummarizer.pipelines.s03_data_transformation_pipeline import DataTransformationPipeline
from textSummarizer.pipelines.s04_model_trainer_pipeline import ModelTrainerPipeline
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

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    data_validation = DataTransformationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e