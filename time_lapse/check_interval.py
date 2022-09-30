import argparse
import datetime
import pathlib

from glob import glob

import exifreader

MARGIN = datetime.timedelta(seconds=0.2)
MIN_IMAGES_SEQUENCE = 5


def get_image_date(image_path):
    """Get EXIF image date from an image as a datetime"""
    with open(image_path, 'rb') as _file:
        tags = exifreader.process_file(_file, details=False)
    date_time = tags['EXIF DateTimeOriginal'].values
    subsec = tags['EXIF SubSecTimeOriginal'].values
    full_date_time = f'{date_time}.{subsec}'
    image_date = datetime.datetime.strptime(full_date_time, '%Y:%m:%d %H:%M:%S.%f')
    return image_date


def find_sequences(pattern, shots_per_interval):
    skip = shots_per_interval
    files = sorted(glob(pattern))
    image_dates = [
        {'path': pathlib.Path(path).name, 'date': get_image_date(path)}
        for path in files[::skip]
    ]

    n_same_interval = 1
    start_of_sequence = image_dates[0]['path']

    print(
        '   n',
        'interval',
        'sequence',
        sep='\t'
    )

    for i, (previous, current, following) in enumerate(zip(image_dates[:-2], image_dates[1:-1], image_dates[2:]), 1):
        n_same_interval += 1

        interval = current['date'] - previous['date']
        new_interval = following['date'] - current['date']

        if abs(interval - new_interval) > MARGIN:
            if n_same_interval > MIN_IMAGES_SEQUENCE:
                print(
                    f'{n_same_interval:4}',
                    f'{interval.total_seconds():7}s',
                    f'{start_of_sequence} → {current["path"]}',
                    sep='\t'
                )
            start_of_sequence = current['path']
            n_same_interval = 1

    n_same_interval += 1

    if n_same_interval > MIN_IMAGES_SEQUENCE:
        print(
            f'{n_same_interval:4}',
            f'{new_interval.total_seconds():7}s',
            f'{start_of_sequence} → {following["path"]}',
            sep='\t'
        )


def find_outliers(pattern, shots_per_interval):
    skip = shots_per_interval
    files = sorted(glob(pattern))
    image_dates = [
        {'path': pathlib.Path(path).name, 'date': get_image_date(path)}
        for path in files[::skip]
    ]
    outliers = []

    n_since_last_change = 0
    previous_interval = datetime.timedelta()

    for i, (previous, current) in enumerate(zip(image_dates[:-1], image_dates[1:]), 1):
        n_since_last_change += 1
        interval = current['date'] - previous['date']
        if previous_interval and abs(interval - previous_interval) > MARGIN:
            outliers.append((interval, previous['path'], current['path']))
            print(
                f'{i:5} – '
                f'{n_since_last_change:4} – '
                f'{previous_interval.total_seconds():6}s → {interval.total_seconds():6}s – '
                f'{previous["path"]} → {current["path"]}'
            )
            n_since_last_change = 0
        previous_interval = interval

    return outliers


def main():
    parser = argparse.ArgumentParser(description='.')
    parser.add_argument(
        '--pattern',
        default='*.NEF',
        help='Regex pattern with which to find the input frames.',
    )
    parser.add_argument(
        '--shots_per_interval',
        type=int,
        default=1,
        help='Number of images per interval, e.g. in case of HDR shots.',
    )
    args = parser.parse_args()

    find_sequences(
        args.pattern,
        args.shots_per_interval,
    )


if __name__ == '__main__':
    main()
