import argparse
import datetime
import pathlib

from dataclasses import dataclass
from operator import attrgetter

import exifreader

MARGIN = datetime.timedelta(seconds=0.2)
MIN_INTERVAL = datetime.timedelta(seconds=0.4)
MIN_IMAGES_SEQUENCE = 20


def get_image_date(image_path: pathlib.Path) -> datetime.datetime:
    """Get EXIF image date from an image as a datetime"""
    with image_path.open('rb') as _file:
        tags = exifreader.process_file(_file, details=False)
    date_time = tags['EXIF DateTimeOriginal'].values
    subsec = tags['EXIF SubSecTimeOriginal'].values
    full_date_time = f'{date_time}.{subsec}+0000'
    image_date = datetime.datetime.strptime(full_date_time, '%Y:%m:%d %H:%M:%S.%f%z')
    return image_date


@dataclass
class ImageInfo:
    path: pathlib.Path
    date: datetime.datetime


def find_sequences(pattern: str, shots_per_interval: int, group: bool) -> None:
    skip = shots_per_interval
    files = sorted(pathlib.Path().glob(pattern))

    if not files:
        print(f'Found no matching files the pattern "{pattern}"')
        return

    image_dates = sorted(
        (ImageInfo(path=path, date=get_image_date(path)) for path in files[::skip]),
        key=attrgetter('date'),
    )

    start_of_sequence = image_dates[0].path
    sequence = [start_of_sequence]
    nth_sequence = 1

    print(
        ' seq',
        '   n',
        'interval',
        'sequence',
        sep='\t',
    )

    for previous, current, following in zip(image_dates[:-2], image_dates[1:-1], image_dates[2:], strict=True):
        sequence.append(current.path)

        interval = current.date - previous.date
        new_interval = following.date - current.date

        if interval < MIN_INTERVAL or abs(interval - new_interval) > MARGIN:
            if len(sequence) > MIN_IMAGES_SEQUENCE:
                print(
                    f'{nth_sequence:4}',
                    f'{len(sequence):4}',
                    f'{interval.total_seconds():7}s',
                    f'{sequence[0]} → {sequence[-1]}',
                    sep='\t',
                )
                if group:
                    group_sequence(sequence, nth_sequence)
                nth_sequence += 1
            sequence = [current.path]

    sequence.append(following.path)
    if len(sequence) > MIN_IMAGES_SEQUENCE:
        print(
            f'{nth_sequence:4}',
            f'{len(sequence):4}',
            f'{new_interval.total_seconds():7}s',
            f'{sequence[0]} → {sequence[-1]}',
            sep='\t',
        )
        if group:
            group_sequence(sequence, nth_sequence)


def group_sequence(sequence: list[pathlib.Path], sequence_number: int) -> None:
    """Group all files in the sequence into a subdirectory in the working directory"""

    pathlib.Path(f'sequence_{sequence_number}').mkdir()
    for path in sequence:
        path.rename(f'sequence_{sequence_number}/{path.name}')


def main() -> None:
    parser = argparse.ArgumentParser(description='.')
    parser.add_argument(
        '--pattern',
        default='*.NEF',
        help='Glob pattern with which to find the input frames.',
    )
    parser.add_argument(
        '--shots_per_interval',
        type=int,
        default=1,
        help='Number of images per interval, e.g. in case of HDR shots.',
    )
    parser.add_argument(
        '--group',
        action='store_true',
        help='Group images in the same interval into directories.',
    )
    args = parser.parse_args()

    find_sequences(
        args.pattern,
        args.shots_per_interval,
        args.group,
    )


if __name__ == '__main__':
    main()
