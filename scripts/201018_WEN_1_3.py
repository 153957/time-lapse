import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/201018_WEN_1/*.tif',  # WEN_058458 - WEN_058786
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/201018_WEN_3/*.tif'  # WEN_058987 - WEN_059196
]
# poster: WEN_058458


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=25)
        .filter_('deflicker', mode='pm', size=2)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=False)


if __name__ == '__main__':
    make_movie()
