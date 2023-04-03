import pandas as pd

from config import PROJECT_PATH, PERCENTAGE_LOWER_LIMIT, Y_LABEL, logger, ROW_DATASET_NUMBER
from .measurement import Measurement


class MeasurementFactory:

    def __init__(self, file_path: str) -> None:
        self._set_data_frame(file_path)

    def _set_data_frame(self, file_path: str) -> None:
        if PROJECT_PATH not in file_path:
            file_path = PROJECT_PATH + '/' + file_path

        if 'csv' in file_path:
            self.data_frame = pd.read_csv(file_path)
        elif 'xls' in file_path:
            self.data_frame = pd.read_excel

    def _get_data_to_append(self, row_index: int, dataset_index: int) -> dict | None:
        postfix = ''
        if dataset_index > 0:
            postfix = f'.{str(dataset_index)}'

        percentage_column_name = f'Percentage{postfix}'
        diameter_column_name = f'Diameter{postfix}'

        percentage = self.data_frame[percentage_column_name][row_index]
        if percentage >= PERCENTAGE_LOWER_LIMIT:

            diameter = self.data_frame[diameter_column_name][row_index]
            return {
                'percentage': percentage,
                'diameter': diameter
            }

        return None

    def get_measurement_list(self) -> list[Measurement]:
        measurements_list = []
        data = []

        prev_y_label = None

        for row_index, y_label in enumerate(self.data_frame[Y_LABEL]):

            if prev_y_label != y_label and prev_y_label is not None:
                measurements_list.append(Measurement(data, prev_y_label))
                data = []

            for dataset_index in range(ROW_DATASET_NUMBER):
                data_to_append = self._get_data_to_append(row_index, dataset_index)

                if data_to_append:
                    data.append(data_to_append)

                prev_y_label = y_label

        if not measurements_list:
            logger.log_empty_measurements_list()

        return measurements_list
