import os

import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/160813_1_Rhein_am_Flammen/*.tiff',  # ARN_105144 - ARN_106213
]
# poster: ARN_105611


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=60)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
