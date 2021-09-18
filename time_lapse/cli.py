import argparse

from time_lapse import output, source


def make_movie(name, patterns, fps, deflicker, watermark, verbose, dryrun):
    source_input = source.get_input(patterns, fps, deflicker)
    output.create_outputs(source_input, name, watermark=watermark, verbose=verbose, dryrun=dryrun)


def main():
    parser = argparse.ArgumentParser(description='Combine frames into a movie.')
    parser.add_argument(
        '--name',
        help='Output name of the movie, without file extension.',
        default='output',
    )
    parser.add_argument(
        '--pattern',
        help='Glob pattern(s) with which to find the input frames.',
        default='*.tiff',
        nargs='+',
    )
    parser.add_argument(
        '--fps',
        help='Frame rate of the created movie.',
        type=int,
        default=30,
        choices=[1, 2, 6, 12, 15, 24, 25, 30, 48, 50, 60, 120, 240, 300],
    )
    parser.add_argument(
        '--deflicker',
        help='Frame window to use for deflicker, off when set to 0.',
        type=int,
        default=0,
    )
    parser.add_argument(
        '--dryrun',
        help='Do not perform the ffmpeg command, only show it.',
        action='store_true',
    )
    parser.add_argument(
        '--quiet',
        help='Produce less output, i.e. no graph and ffmpeg command.',
        action='store_false',
    )
    parser.add_argument(
        '--watermark',
        help='Add watermark, provide two value, one main text and the subtext.',
        nargs=2,
    )
    args = parser.parse_args()

    make_movie(args.name, args.pattern, args.fps, args.deflicker, args.watermark, args.quiet, args.dryrun)


if __name__ == '__main__':
    main()
