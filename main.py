from measurement.measurement_factory import MeasurementFactory
from setup import setup
from view.report_builder import ReportBuilder

if __name__ == '__main__':
    setup()

    measurement_factory = MeasurementFactory('input/test.csv')
    measurement_list = measurement_factory.get_measurement_list()

    report_builder = ReportBuilder(measurement_list)
    report_builder.build_csv()
