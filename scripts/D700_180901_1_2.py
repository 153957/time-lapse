import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/180901/1/*.tiff',  # ADL_242138 - ADL_242499
    '/Volumes/Falcon/tl_temp/180901/2/*.tiff',  # ADL_242506 - ADL_243212
]


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=10)
        .filter_('deflicker', mode='pm', size=2)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
