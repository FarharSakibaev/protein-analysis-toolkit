from dimension.dimension_factory import DimensionFactory
from view.report_builder import ReportBuilder

if __name__ == '__main__':
    dimension_factory = DimensionFactory('input/test.csv')
    dimension_list = dimension_factory.get_dimension_list()

    report_builder = ReportBuilder(dimension_list)
    report_builder.build_csv()
