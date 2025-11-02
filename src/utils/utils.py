# utils.py

import os
import json
import logging
from datetime import datetime
from typing import List

class Utils:
    @staticmethod
    def get_current_timestamp() -> str:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def load_json(file_path: str) -> dict:
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def save_json(data: dict, file_path: str) -> None:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def format_file_path(file_path: str) -> str:
        return os.path.abspath(file_path)

    @staticmethod
    def get_available_files(folder_path: str) -> List[str]:
        return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    @staticmethod
    def get_logger() -> logging.Logger:
        logger = logging.getLogger('user-dashboard')
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler('dashboard.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger