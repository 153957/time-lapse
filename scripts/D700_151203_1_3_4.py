import ffmpeg

from time_lapse import output

NAME = 'D700_151203_1_3_4'
PATTERNS = [
    '/Volumes/Falcon/tl_temp/151203/1/*.tiff',  # ADL_197037 - ADL_197259
    '/Volumes/Falcon/tl_temp/151203/3/*.tiff',  # ADL_197298 - ADL_197378 & ADL_197386 - ADL_197534
    '/Volumes/Falcon/tl_temp/151203/4/*.tiff',  # ADL_197555 - ADL_197678
]


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=24)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
