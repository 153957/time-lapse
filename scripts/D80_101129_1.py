import ffmpeg

from time_lapse import output

NAME = 'D80_101129_1'
PATTERN1 = '/Volumes/Falcon/tl_temp/101129_1/*.tiff'  # D80_101129_171323 - D80_101129_174150


def make_movie():
    input1 = (
        ffmpeg
        .input(PATTERN1, pattern_type='glob', framerate=24)
        .filter_('deflicker', mode='pm', size=10)
    )
    output.create_outputs(input1, NAME, verbose=True)


if __name__ == '__main__':
    make_movie()
