import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN1 = '/Volumes/Falcon/tl_temp/121103_2/*.tiff'  # ARN_020512 - ARN_021511
# poster: ARN_020512


def make_movie():
    input1 = (
        ffmpeg
        .input(PATTERN1, pattern_type='glob', framerate=30)
        # .filter_('deflicker', mode='pm', size=2)
    )
    output.create_outputs(input1, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
