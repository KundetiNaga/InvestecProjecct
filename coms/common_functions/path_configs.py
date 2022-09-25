import os
from pathlib import Path


class PathConfigs:
    parentDir = Path(__file__).parent.parent.parent  # get parent directory

    targetDataPath = os.path.join(parentDir, 'testdata')

    investec_json_rd_file_path = os.path.join(parentDir, 'testdata', 'investecApi.json')