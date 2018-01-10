import ffmpeg

from time_lapse import output

NAME = 'D500_170909_1'
PATTERN = '/Users/arne/Movies/170909_1_sample/*.tiff'


def make_movie():
    input = (
        ffmpeg
        .input(PATTERN, pattern_type='glob', framerate=24)
        .filter_('deflicker', mode='pm', size=10)
    )
    output.create_outputs(input, NAME, verbose=False)


if __name__ == '__main__':
    make_movie()
