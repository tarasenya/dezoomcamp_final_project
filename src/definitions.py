"""
Defining some constants used in code.
"""
from configparser import ConfigParser

config_parser = ConfigParser()
config_parser.read(filenames='config.ini')

project_name = config_parser.get('GCP', 'project')
dataset = config_parser.get('GCP', 'dataset')
table_name = config_parser.get('GCP', 'table_name')
bucket_name = config_parser.get('GCP', 'bucket_name')

HISTORICAL_DATA = 'historical_koala_data'
HEALTH_DATA = 'health_koala_data'
