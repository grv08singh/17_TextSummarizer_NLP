import os
from textSummarizer.logging import logger
from textSummarizer.config.configuration import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_files_exist(self) -> bool:
        logger.info("Checking if all required files are present...")
        try:
            validation_status = None
            all_dir = os.listdir(os.path.join("artifacts", "data_ingestion", "data", "samsum_dataset"))

            for file in all_dir:
                if file not in self.config.ALL_REQUIRED_FILES:
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
            logger.info("All required files are present.")
            return validation_status
        except Exception as e:
            raise e