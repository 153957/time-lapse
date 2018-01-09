import ffmpeg

from time_lapse import output, watermark


if __name__ == '__main__':
    name = 'D500_170909_1'
    pattern = '/Users/arne/Movies/170909_1_sample/*.tiff'

    input = (ffmpeg
        .input(pattern, pattern_type='glob', framerate=24)
        .filter_('deflicker', mode='pm', size=10)
    )
    output.create_outputs(input, name, verbose=False)
