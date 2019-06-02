import datetime
import os

from glob import glob

from PIL import Image

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    ('/Volumes/Archive/tl_temp/D80_110522_1/*.tiff', 48),  # DSC_163723 - DSC_164490
    ('/Volumes/Archive/tl_temp/D80_110522_2/*.tiff', 48),  # DSC_164783 - DSC_165480
    ('/Volumes/Archive/tl_temp/D80_110521_4/*.tiff', 24),  # DSC_162504 - DSC_162918
    ('/Volumes/Archive/tl_temp/D80_110521_2/*.tiff', 24),  # DSC_162181 - DSC_162301
    ('/Volumes/Archive/tl_temp/D80_110515_3/*.tiff', 24),  # DSC_158888 - DSC_159150
]


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=rate)
        .filter_('deflicker', mode='pm', size=10)
        for pattern, rate in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True, framerate=48)


def get_image_date(image_path):
    """Get EXIF image date from an image as a datetime"""
    return datetime.datetime.strptime(Image.open(image_path)._getexif()[36867], '%Y:%m:%d %H:%M:%S')


def analyse_interval_between_frames():
    files = glob(PATTERNS[2][0])  # D80_110521_4
    outliers = []
    correct_interval = 4

    for cur_path, nex_path in zip(files[:-1], files[1:]):
        dt = get_image_date(nex_path) - get_image_date(cur_path)
        if dt > datetime.timedelta(seconds=correct_interval):
            print(dt, nex_path)
            outliers.append(int(nex_path[-10:-4]))

    [(x, x - y) for z, x, y in zip(outliers[1:], outliers[:-1])]


if __name__ == '__main__':
    make_movie()
