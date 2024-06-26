from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_bucket: str
    source_object_key: str
    local_data_file: Path
    unzip_dir: Path
