import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from textSummarizer.config.configuration import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)
        target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        try:
            logger.info("entered convert method in class DataTransformation")
            dataset_samsum = load_from_disk(self.config.data_path)
            self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name, use_fast=False)
            dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True, num_proc=1)
            dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))
            logger.info("exited convert method in class DataTransformation")
        except Exception as e:
            logger.info(f"error in convert method in class DataTransformation: {e}")
            raise e