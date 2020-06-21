import glob

import ffmpeg


def files_with_audio(pattern='*.mp4'):
    for filename in glob.glob(pattern):
        for stream in ffmpeg.probe(filename)['streams']:
            if stream['codec_type'] == 'audio':
                yield filename
