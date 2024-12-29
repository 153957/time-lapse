"""Function related to detecting audio in movies."""
from collections.abc import Iterator
from pathlib import Path

import ffmpeg


def files_with_audio(pattern: str = '*.mp4') -> Iterator[str]:
    """Find files matching the provided pattern with an audio stream.

    :param pattern: glob pattern to find files to check.
    :returns: Iterator over the found files with an audio stream.

    """
    for filename in Path().glob(pattern):
        if any(
            stream['codec_type'] == 'audio'
            for stream in ffmpeg.probe(filename)['streams']
        ):
            yield str(filename)
