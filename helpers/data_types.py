from enum import Enum


class FileType:
    def __init__(self, extension, type_):
        self.extension = extension
        self.type = type_


class AvailableFileTypes(Enum):
    CSV = FileType('csv', 'CSV')
    JSON = FileType('json', 'JSON')

    @staticmethod
    def get_available_types():
        return [item.value.type for item in AvailableFileTypes]

    @staticmethod
    def get_available_types_string():
        return ', '.join(AvailableFileTypes.get_available_types())
