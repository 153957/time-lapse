import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/180628_1/*.tiff',  # APL_027178 - APL_027581
]
# poster: APL_027521


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=25)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
