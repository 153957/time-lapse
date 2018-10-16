import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/181014/1/*.tiff',  # ADL_244715 - ADL_244857
    '/Volumes/Falcon/tl_temp/181014/2/*.tiff',  # ADL_244862 - ADL_245077
]


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=24)
        .filter_('deflicker', mode='pm', size=10)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
