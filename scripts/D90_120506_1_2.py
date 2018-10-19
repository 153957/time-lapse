import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN1 = '/Volumes/Falcon/tl_temp/120506_1/*.tiff'
PATTERN2 = '/Volumes/Falcon/tl_temp/120506_2/*.tiff'


def make_movie():
    input1 = (
        ffmpeg
        .input(PATTERN1, pattern_type='glob', framerate=48)
        .filter_('deflicker', mode='pm', size=10)
        .filter_('scale', size='hd1080', force_original_aspect_ratio='increase')
    )
    input2 = (
        ffmpeg
        .input(PATTERN2, pattern_type='glob', framerate=48)
        .filter_('deflicker', mode='pm', size=10)
    )
    input = ffmpeg.concat(input1, input2)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
