import json
import csv
import os
from abc import abstractmethod
from pathlib import Path


class FileWorker:
    output_directory = 'output'

    def __init__(self, output_type, output_file_name):
        self.output_directory_path = os.path.join(FileWorker.output_directory, output_type)
        self.output_file_path = os.path.join(self.output_directory_path, output_file_name)

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class CSVWorker(FileWorker):
    def __init__(self):
        super().__init__('csv', 'all.csv')

        self.input_file_path = os.path.join('input/input.csv')

    def read(self):
        results = []

        with open(self.input_file_path) as csv_file:
            reader = csv.reader(csv_file)
            header = []
            for index, row in enumerate(reader):
                if index == 0:
                    header = row
                else:
                    results.append(dict(zip(header, row)))

        return results

    def write(self, data):  # data here is a list of dicts: [{}, {}]
        Path(self.output_directory_path).mkdir(parents=True, exist_ok=True)

        if len(data) == 0:
            open(self.output_file_path, 'w').close()
        else:
            keys = data[0].keys()
            data_from_list = [item.values() for item in data]

            with open(self.output_file_path, 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(keys)
                writer.writerows(data_from_list)


class JSONWorker(FileWorker):
    def __init__(self):
        super().__init__('json', 'all.json')

        self.input_file_path = os.path.join('input/input.json')

    def read(self):
        with open(self.input_file_path) as json_file:
            products = json.load(json_file)

        return products

    def write(self, data):
        pass
