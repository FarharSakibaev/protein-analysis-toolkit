import sys

from loguru import logger

logger.remove(handler_id=None)
logger.add(sink='logs.log', level='DEBUG')
logger.add(sink=sys.stdout, level='INFO')


class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self.logs = {}
        self.messages = {
            'get_measurement_list': 'Measurements added for y labels',
            '_sort_percentage': 'Excluded values',
            '_calculate': 'No percentage found for y labels'
        }

    def release_logs(self, func: callable):
        def wrapper(called_obj, *args):
            data = func(called_obj, *args)

            name = func.__name__
            message = self.messages[name] + ': \n' + str(self.logs[name])

            logger.info(message)
            return data

        return wrapper

    def log_new_measurement(self, y_label):
        if 'get_measurement_list' not in self.logs:
            self.logs['get_measurement_list'] = []

        self.logs['get_measurement_list'].append(y_label)

    @staticmethod
    def log_empty_measurements_list():
        logger.info('No measurements found')

    @staticmethod
    def log_low_percentage(percentage):
        logger.debug('Low percentage: ' + str(percentage))

    def log_exclusion(self, data):
        if '_sort_percentage' not in self.logs:
            self.logs['_sort_percentage'] = []

        self.logs['_sort_percentage'].append(data)

    def log_empty_y_label_values(self, data):
        if '_calculate' not in self.logs:
            self.logs['_calculate'] = []

        self.logs['_calculate'].append(data)

    @staticmethod
    def log_config(config):
        logger.debug('Current config: ' + str(config))
