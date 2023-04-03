import csv

from config import OUTPUT_PATH, Y_LABEL
from dimension.dimension import Dimension


class ReportBuilder:

    def __init__(self, data_sheet_list: list[Dimension], file_name: str = 'out.csv') -> None:
        self.data_sheet_list = data_sheet_list
        self.csv_path = OUTPUT_PATH + '/' + file_name

    def build_csv(self) -> None:
        data_to_out = [[Y_LABEL, 'autolysis', 'native', 'small_aggregates', 'large_aggregates']]

        for data_sheet in self.data_sheet_list:
            data_to_out.append([
                data_sheet.get_y_label_value(),
                data_sheet.get_autolysis(),
                data_sheet.get_native(),
                data_sheet.get_small_aggregates(),
                data_sheet.get_large_aggregates(),
            ])

        with open(self.csv_path, 'w') as output:
            writer = csv.writer(output)
            writer.writerows(data_to_out)
