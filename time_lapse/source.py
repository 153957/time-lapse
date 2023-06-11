import ffmpeg


def get_input(
    patterns: list[str] | str,
    fps: int,
    deflicker: int,
    filters: list[tuple[str, dict[str, str]]] | None,
) -> ffmpeg.nodes.FilterNode:
    """Find input files and set framerate and deflickering

    :param patterns: glob pattern(s) to find input frames.
    :param fps: framerate of the output video.
    :param deflicker: frame window to use for deflickering.
    :param filters: list of tuples, each tuple being two-tuple containing
        the filter name and a dictionary with arguments for the filter.

    """
    if isinstance(patterns, str):
        patterns = [patterns]

    pattern_inputs = [ffmpeg.input(pattern, pattern_type='glob', framerate=fps) for pattern in patterns]

    if filters:
        for filter_name, filter_arguments in filters:
            pattern_inputs = [pattern_input.filter(filter_name, **filter_arguments) for pattern_input in pattern_inputs]

    if deflicker:
        pattern_inputs = [
            pattern_input.filter('deflicker', mode='pm', size=deflicker) for pattern_input in pattern_inputs
        ]

    return ffmpeg.concat(*pattern_inputs)
