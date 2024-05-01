from linear_regressor import logger
from linear_regressor.constants import *
from linear_regressor.pipeline.stage_01_data_ingestion import DataIngestionPipeline

try:
    logger.info(f"----- Stage {DATA_INGESTION_STAGE_NAME} started -----")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"----- Stage {DATA_INGESTION_STAGE_NAME} completed -----")
except Exception as e:
    logger.exception(e)
    raise e
