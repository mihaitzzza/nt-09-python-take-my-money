import argparse
from helpers.constants import AVAILABLE_FILE_TYPES
from stats.base import Stats

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Importer/exporter for US client.')
    parser.add_argument(
        '-i',
        '--input_type',
        help=f'Type of file where we read from. {AVAILABLE_FILE_TYPES}',
        dest='input_type',
        default='csv'
    )
    parser.add_argument(
        '-o',
        '--output_type',
        help=f'Type of file where we write to. {AVAILABLE_FILE_TYPES}',
        dest='output_type',
        default='json'
    )

    args = parser.parse_args()
    args = vars(args)  # call to __dict__ magic method

    stats = Stats(**args)  # Stats(args.get('input_type'), args.get('output_type'))
    stats.run()
