import logging.config
from os import path

pytest_plugins = [
        'src.browser'
]

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(log_file_path)