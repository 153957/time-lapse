import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Archive/Other/Time-lapse Wen/timelapse_bloem_wen/Output/200530_D700_bloem/WEN_*.tif',  # WEN_D700_77936 - WEN_D700_79236
]


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=30)
        .filter_('deflicker', mode='pm', size=4)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True, watermark=False)


if __name__ == '__main__':
    make_movie()
