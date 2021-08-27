import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Chiss/Falcon/Time-Lapse/WEN_1_Food/WEN_*.tif',  # WEN_052204 - WEN_052527
]
# poster: WEN_052257


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=25)
        .filter_('deflicker', mode='pm', size=2)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
