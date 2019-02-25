import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/181021_1/*.tiff',  # ADL_248271 - ADL_249074
    '/Volumes/Falcon/tl_temp/181019_2/*.tiff',  # ADL_246049 - ADL_247034
    '/Volumes/Falcon/tl_temp/181021_2/*.tiff',  # ADL_249084 - ADL_249805
    '/Volumes/Falcon/tl_temp/181020_1/*.tiff',  # ADL_247427 - ADL_248067
    '/Volumes/Falcon/tl_temp/181019_3/*.tiff',  # ADL_247060 - ADL_247415
    '/Volumes/Falcon/tl_temp/181020_2/*.tiff',  # ADL_248070 - ADL_248261
]


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=24)
        .filter_('deflicker', mode='pm', size=3)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
