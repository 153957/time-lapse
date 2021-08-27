import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/160813_1_Boot/*.tiff',  # ADL_216004 - ADL_216758
    '/Volumes/Falcon/tl_temp/160813_2_Boot/*.tiff',  # ADL_216765 - ADL_217317
]
# poster: ADL_216065


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=30)
        .filter_('deflicker', mode='pm', size=3)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
