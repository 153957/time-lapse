import ffmpeg

OUTPUT_OPTIONS = {
    'crf': 20,
    'preset': 'slower',
    'movflags': 'faststart',
    'pix_fmt': 'yuv420p'
}

BOTTOM_RIGHT = {
    'x': 'main_w-overlay_w',
    'y': 'main_h-overlay_h'
}


def create_outputs(input, name, verbose=False, dry_run=False):
    """Create output at multiple sizes

    :param input: ffmpeg input node ready for scaling and conversion.
    :param name: name of the output.
    :param verbose: if True output the ffmpeg CLI command which will be used.
    :param dry_run: if True the command will not be run.

    """
    output = ffmpeg.merge_outputs(
        # 3840x2160
        input[0]
            .filter_('scale', size='uhd2160', force_original_aspect_ratio='increase')
            .overlay(watermark(), **BOTTOM_RIGHT)
            .output(f'{name}_3840.mp4', **OUTPUT_OPTIONS),
        # 1920x1080
        input[1]
            .filter_('scale', size='hd1080', force_original_aspect_ratio='increase')
            .overlay(watermark, **BOTTOM_RIGHT)
            .output(f'{name}_1920.mp4', **OUTPUT_OPTIONS),
        # 960x540
        input[2]
            .filter_('scale', size='qhd', force_original_aspect_ratio='increase')
            .overlay(watermark, **BOTTOM_RIGHT)
            .output(f'{name}_960.mp4', **OUTPUT_OPTIONS),
    )

    if verbose:
        ' '.join(output.get_args())
        output.view(filename=f'{name}.pdf')

    if not dry_run:
        output..run()

    return output
