import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/171119_APL_3/*.tif',  # APL_010583 - APL_010757
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/171119_APL_2/*.tif',  # APL_009696 - APL_010553
]
# poster: APL_009714


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=25)
        .filter_('deflicker', mode='pm', size=2)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=False)


if __name__ == '__main__':
    make_movie()
