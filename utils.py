import json
import logging
import os
import pathlib
import time
from datetime import datetime

class FileUtil:
    @staticmethod
    def read_json_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            logging.error(f"Failed to decode JSON from file: {file_path}")
            return None
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            return None

    @staticmethod
    def write_json_file(file_path, data):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            logging.error(f"Failed to write to file: {file_path}")
            raise e

    @staticmethod
    def read_text_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            return None

    @staticmethod
    def write_text_file(file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            return True
        except Exception as e:
            logging.error(f"Failed to write to file: {file_path}")
            raise e

    @staticmethod
    def get_timestamp():
        return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    @staticmethod
    def get_dir_size(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    @staticmethod
    def get_files_in_dir(path):
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    @staticmethod
    def get_subdirectories_in_dir(path):
        return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]