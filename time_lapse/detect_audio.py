from collections.abc import Iterator
from pathlib import Path

import ffmpeg


def files_with_audio(pattern: str = '*.mp4') -> Iterator[str]:
    for filename in Path().glob(pattern):
        for stream in ffmpeg.probe(filename)['streams']:
            if stream['codec_type'] == 'audio':
                yield str(filename)
