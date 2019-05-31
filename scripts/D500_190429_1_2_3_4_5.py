import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/190429_4_Waterfall/*.tiff',  # APL_049902 - APL_050084
    '/Volumes/Falcon/tl_temp/190429_5_Waterfall/*.tiff',  # APL_050155 - APL_050292
    '/Volumes/Falcon/tl_temp/190429_6_Waterfall/*.tiff',  # APL_050300 - APL_050457
    '/Volumes/Falcon/tl_temp/190429_1_Waterfall/*.tiff',  # APL_049154 - APL_049439
    '/Volumes/Falcon/tl_temp/190429_2_Waterfall/*.tiff',  # APL_049481 - APL_049696
    '/Volumes/Falcon/tl_temp/190429_3_Waterfall/*.tiff',  # APL_049698 - APL_049888
]


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=30)
        .filter_('deflicker', mode='pm', size=4)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
