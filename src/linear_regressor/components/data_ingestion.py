from linear_regressor import logger
from linear_regressor.entity.config_entity import DataIngestionConfig
import zipfile
from boto3 import Session
import os


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        session = Session()
        s3 = session.resource('s3')

        try:
            bucket = self.config.source_bucket
            object_key = self.config.source_object_key
            local_file = self.config.local_data_file
            s3.Bucket(bucket).download_file(object_key, local_file)
            logger.info(f'Raw data downloaded from s3://{bucket}/{object_key} to {local_file}')
        except Exception as e:
            raise e

    def extract_data(self, delete_zip=False):
        local_file = self.config.local_data_file
        unzip_path = self.config.unzip_dir

        with zipfile.ZipFile(local_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f'Data successfully extracted from: {local_file}')

        if delete_zip:
            os.remove(local_file)
            logger.info(f'Zip file: {local_file} deleted')
