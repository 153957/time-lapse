import ffmpeg


def get_input(patterns, fps, deflicker):
    """Find input files and set framerate and deflickering

    :param patterns: glob pattern(s) to find input frames.
    :param fps: framerate of the output video.
    :param deflicker: frame window to use for deflickering,

    """
    if isinstance(patterns, str):
        patterns = [patterns]

    return ffmpeg.concat(*[
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=fps)
        .filter('deflicker', mode='pm', size=deflicker)
        for pattern in patterns
    ])
