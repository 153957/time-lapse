import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/181012_1/*.tiff',  # ADL_243737 - ADL_244687
]
# poster: ADL_244569


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=30)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
