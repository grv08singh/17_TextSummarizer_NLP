from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info("Entered main method in DataTransformationPipeline")
            config_manager = ConfigurationManager()
            data_transformation_config = config_manager.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
            logger.info("Exited main method in DataTransformationPipeline")
        except Exception as e:
            logger.info(f"error in data transformation pipeline main method: {e}")
            raise e

if __name__ == "__main__":
    try:
        logger.info(">>>>>>>>>>>>>>>>>>>>> Pipeline s03_data_transformation_pipeline started <<<<<<<<<<<<<<<<<")
        pipeline = DataTransformationPipeline()
        pipeline.main()
        logger.info(">>>>>>>>>>>>>>>>>>>>> Pipeline s03_data_transformation_pipeline completed <<<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e