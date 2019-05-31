import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/190430_1_Waterfall/*.tiff',  # APL_050876 - APL_051061
]


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=24)
        .filter_('deflicker', mode='pm', size=2)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
