from linear_regressor.config.configuration import ConfigurationManager
from linear_regressor.components.data_ingestion import DataIngestion
from linear_regressor.constants import *

from linear_regressor import logger


class DataIngestionPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.extract_data(delete_zip=True)
        except Exception as e:
            raise e


if __name__ == '__main__':
    try:
        logger.info(f"----- Stage {DATA_INGESTION_STAGE_NAME} started -----")
        DataIngestionPipeline().main()
        logger.info(f"----- Stage {DATA_INGESTION_STAGE_NAME} completed -----")
    except Exception as ex:
        logger.exception(ex)
        raise ex
