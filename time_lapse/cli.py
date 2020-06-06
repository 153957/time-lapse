import argparse

import ffmpeg

from time_lapse import output


def make_movie(name, pattern, fps, deflicker):
    input = (
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=fps)
    )
    if deflicker:
        input = input.filter_('deflicker', mode='pm', size=deflicker)

    output.create_outputs(input, name, verbose=True, watermark=False)


def main():
    parser = argparse.ArgumentParser(description='Combine frames into a movie.')
    parser.add_argument(
        '--name',
        default='output',
        help='Output name of the movie, without file extension.'
    )
    parser.add_argument(
        '--pattern',
        default='*.tiff',
        help='Regex pattern with which to find the input frames.'
    )
    parser.add_argument(
        '--fps',
        help='Frame rate of the created movie.',
        type=int,
        default=30,
        choices=[1, 2, 6, 12, 15, 24, 25, 30, 48, 50, 60, 120, 240, 300]
    )
    parser.add_argument(
        '--deflicker',
        help='Frame window to use for deflicker, off when set to 0.',
        type=int,
        default=0
    )
    args = parser.parse_args()

    make_movie(args.name, args.pattern, args.fps, args.deflicker)


if __name__ == '__main__':
    main()
