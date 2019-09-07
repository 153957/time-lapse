import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/130305_1/*.tiff',  # ARN_038167 - ARN_038476
    '/Volumes/Falcon/tl_temp/130305_2/*.tiff',  # ARN_038495 - ARN_039026
]
# poster: ARN_038262


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=48)
        .filter_('deflicker', mode='pm', size=10)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
