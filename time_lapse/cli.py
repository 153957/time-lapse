"""Function called by the CLI."""

import argparse

from time_lapse import output, source
from time_lapse.detect_audio import files_with_audio


def make_movie(
    name: str,
    patterns: list[str] | str,
    fps: int,
    deflicker: int,
    watermark: bool | list[str],
    verbose: bool,
    dryrun: bool,
    filters: list[tuple[str, dict[str, str]]] | None = None,
) -> None:
    """Detect which movie files have an audio stream steered via the CLI.

    :param name: Output name of the movie, without file extension.
    :param patterns: Glob pattern(s) with which to find the input frames.
    :param fps: Frame rate of the created movie.
    :param deflicker: Frame window to use for deflicker, off when set to 0..
    :param watermark: Enable or disable watermark. For custom watermark provide two
        values, one main text and the subtext.
    :param verbose: When enabled the output is more verbose, showing the ffmpeg
        command and the filter graph.
    :param dryrun: When enabled the ffmpeg command is not actually executed.
    :param filters: A list of additional filters to apply to the movie.

    """
    source_input = source.get_input(patterns, fps, deflicker, filters)
    output.create_outputs(source_input, name, watermark=watermark, verbose=verbose, dryrun=dryrun)


def get_parser_timelapse() -> argparse.ArgumentParser:
    """Get argument parser for the timelapse cli."""
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
        dest='patterns',
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
        dest='verbose',
    )
    parser.add_argument(
        '--watermark',
        help='Add watermark, provide two values, one main text and the subtext.',
        nargs=2,
    )
    return parser


def timelapse() -> None:
    """Create a movie steered via the CLI."""
    parser = get_parser_timelapse()
    kwargs = vars(parser.parse_args())

    make_movie(**kwargs)


def get_parser_detect_audio() -> argparse.ArgumentParser:
    """Get argument parser for the detect_audio cli."""
    parser = argparse.ArgumentParser(description='Find movie files with audio streams.')
    parser.add_argument(
        '--pattern',
        help='Glob pattern with which to find the movies to check.',
        default='*.mp4',
    )
    return parser


def detect_audio() -> None:
    """Detect which movie files have an audio stream steered via the CLI."""
    parser = get_parser_detect_audio()
    kwargs = vars(parser.parse_args())

    for filename in files_with_audio(**kwargs):
        print(filename)
