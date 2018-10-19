import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN1 = '/Volumes/Falcon/tl_temp/140416_1/*.tiff'
PATTERN2 = '/Volumes/Falcon/tl_temp/140417_1/*.tiff'


def make_movie():
    input1 = (
        ffmpeg
        .input(PATTERN1, pattern_type='glob', framerate=48)
        .filter_('deflicker', mode='pm', size=10)
    )
    input2 = (
        ffmpeg
        .input(PATTERN2, pattern_type='glob', framerate=48)
        .filter_('deflicker', mode='pm', size=10)
    )
    input = ffmpeg.concat(input2, input1)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
