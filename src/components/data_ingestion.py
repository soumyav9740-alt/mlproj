import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self, data_source: str) -> tuple:
        logging.info("Starting data ingestion process")

        try:
            # Read the dataset
            df = pd.read_csv(data_source)
            logging.info("Dataset read successfully")

            # Create artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info(f"Raw data saved at {self.ingestion_config.raw_data_path}")

            # Split the dataset into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Dataset split into training and testing sets")

            # Save training data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            logging.info(f"Training data saved at {self.ingestion_config.train_data_path}")

            # Save testing data
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info(f"Testing data saved at {self.ingestion_config.test_data_path}")

            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            logging.error("Error occurred during data ingestion", exc_info=True)
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion(data_source='/Users/soumyaverma/Documents/MLproj/notebook/data/stud.csv')

