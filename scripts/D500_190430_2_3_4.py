import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/190430_2_Waterfall/*.tiff',  # APL_051279 - APL_051377
    '/Volumes/Falcon/tl_temp/190430_3_Waterfall/*.tiff',  # APL_051518 - APL_051747
    '/Volumes/Falcon/tl_temp/190430_4_Waterfall/*.tiff',  # APL_051753 - APL_051862
]


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
