from collections import defaultdict
from helpers.data_types import AvailableFileTypes
from .file_workers import CSVWorker, JSONWorker


class Stats:
    def __init__(self, input_type, output_type):
        available_types_lower = [item.lower() for item in AvailableFileTypes.get_available_types()]
        if input_type not in available_types_lower:
            raise TypeError(f'{input_type} is not an available type')

        if output_type not in available_types_lower:
            raise TypeError(f'{output_type} is not an available type.')

        self.input_type = input_type
        self.output_type = output_type
        self.input_file_worker = None
        self.output_file_worker = None

        if self.input_type == 'csv':
            self.input_file_worker = CSVWorker()
        elif self.input_type == 'json':
            self.input_file_worker = JSONWorker()

        if self.output_type == 'csv':
            self.output_file_worker = CSVWorker()
        elif self.output_type == 'json':
            self.output_file_worker = JSONWorker()

    def run(self):
        # Step 1. Read from input file
        products = self.input_file_worker.read()

        # Step 2. Do some magic
        products_by_color = defaultdict(list)
        for product in products:
            products_by_color[product['color']].append(product)

        # Step 3. Write to output file
        for color, products in products_by_color.items():
            self.output_file_worker.write(color, products)
