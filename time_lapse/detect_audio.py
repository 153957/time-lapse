import glob

from collections.abc import Iterator

import ffmpeg


def files_with_audio(pattern: str='*.mp4') -> Iterator[str]:
    for filename in glob.glob(pattern):
        for stream in ffmpeg.probe(filename)['streams']:
            if stream['codec_type'] == 'audio':
                yield filename
