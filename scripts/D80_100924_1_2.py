import ffmpeg

from time_lapse import output

NAME = 'D80_100924_1_2'
PATTERN1 = '/Volumes/Falcon/tl_temp/100924_1/*.tiff'
PATTERN2 = '/Volumes/Falcon/tl_temp/100924_2/*.tiff'


def make_movie():
    input1 = (
        ffmpeg
        .input(PATTERN1, pattern_type='glob', framerate=24)
        .filter_('deflicker', mode='pm', size=10)
    )
    input2 = (
        ffmpeg
        .input(PATTERN2, pattern_type='glob', framerate=48)
        .filter_('deflicker', mode='pm', size=10)
    )
    input = ffmpeg.concat(input1, input2)

    output.create_outputs(input, NAME, verbose=True, r=48)


if __name__ == '__main__':
    make_movie()