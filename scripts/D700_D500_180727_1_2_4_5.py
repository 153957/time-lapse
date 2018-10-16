import ffmpeg

from time_lapse import output

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/180727_Moon/1_D700/*.tiff',  # ADL_240651 - ADL_240862
    '/Volumes/Falcon/tl_temp/180727_Moon/2_D700/*.tiff',  # ADL_240867 - ADL_241048
    '/Volumes/Falcon/tl_temp/180727_Moon/3_D500/*.tiff',  # APL_030936 - APL_031065
    '/Volumes/Falcon/tl_temp/180727_Moon/4_D500/*.tiff',  # APL_031073 - APL_031230
    '/Volumes/Falcon/tl_temp/180727_Moon/5_D700/*.tiff',  # ADL_241162 - ADL_241328
]


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=25)
        .filter_('deflicker', mode='pm', size=10)
        for pattern in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
