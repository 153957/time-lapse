import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/180430_1_Loch_Lomond/*.tiff',  # APL_022590 - APL_022733
    '/Volumes/Falcon/tl_temp/180430_2_Loch_Lomond/*.tiff',  # APL_022748 - APL_022928
]


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=48)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
