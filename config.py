import json
import os

from logs.logger import Logger

logger = Logger()

COLUMNS_HEADER_MAPPING = []
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = f'{PROJECT_PATH}/output'

with open(f'{PROJECT_PATH}/config.json') as config_file:
    config_data = json.load(config_file)
    logger.log_config(config_data)

    PERCENTAGE_LOWER_LIMIT = config_data['percentage_lower_limit']

    AUTOLYSIS_LOWER_LIMIT_SIZE = config_data['autolysis_lower_limit_size']
    AUTOLYSIS_UPPER_LIMIT_SIZE = config_data['autolysis_upper_limit_size']

    NATIVE_LOWER_LIMIT_SIZE = config_data['native_lower_limit_size']
    NATIVE_UPPER_LIMIT_SIZE = config_data['native_upper_limit_size']

    SMALL_AGGREGATES_LOWER_LIMIT_SIZE = config_data['small_aggregates_lower_limit_size']
    SMALL_AGGREGATES_UPPER_LIMIT_SIZE = config_data['small_aggregates_upper_limit_size']

    LARGE_AGGREGATES_LOWER_LIMIT_SIZE = config_data['large_aggregates_lower_limit_size']
    LARGE_AGGREGATES_UPPER_LIMIT_SIZE = config_data['large_aggregates_upper_limit_size']

    EXCLUSION_LOWER_LIMIT = config_data['exclusion_lower_limit']
    EXCLUSION_UPPER_LIMIT = config_data['exclusion_upper_limit']

    Y_LABEL = config_data['y_label']
    ROW_DATASET_NUMBER = config_data['row_dataset_number']

    DECIMAL_PLACES = config_data['decimal_places']
    FETCH_UPDATES = config_data['fetch_updates']

