import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN1 = '/Volumes/Falcon/tl_temp/121004_1/*.tiff'  # ARN_018617 - ARN_019151
# poster: ARN_018617


def make_movie():
    input = (
        ffmpeg
        .input(PATTERN1, pattern_type='glob', framerate=48)
        .filter_('deflicker', mode='pm', size=5)
    )
    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
