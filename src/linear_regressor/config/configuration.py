from linear_regressor.constants import *
from linear_regressor.utils.commons import *
from linear_regressor.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH, params_file_path = PARAMS_FILE_PATH):
        self.config = load_yaml(config_file_path)
        self.params = load_yaml(params_file_path)
        create_directories(
            [self.config.artifacts_root, self.config.data_ingestion.root_dir, self.config.data_ingestion.unzip_dir]
        )

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        data_ingestion_config = DataIngestionConfig(
            root_dir = self.config.data_ingestion.root_dir,
            source_bucket=self.config.data_ingestion.source_bucket,
            source_object_key=self.config.data_ingestion.source_object_key,
            local_data_file=self.config.data_ingestion.local_data_file,
            unzip_dir=self.config.data_ingestion.unzip_dir
        )
        return data_ingestion_config
