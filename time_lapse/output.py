import ffmpeg

from .watermark import add_watermark

OUTPUT_OPTIONS = {
    'crf': 20,
    'preset': 'slower',
    'movflags': 'faststart',
    'pix_fmt': 'yuv420p'
}


def create_outputs(input, name, verbose=False, dry_run=False):
    """Create output at multiple sizes

    :param input: ffmpeg input node ready for scaling and conversion.
    :param name: name of the output.
    :param verbose: if True output the ffmpeg CLI command which will be used.
    :param dry_run: if True the command will not be run.

    """
    split_input = input.split()

    output = ffmpeg.merge_outputs(
        # 3840x2160
        add_watermark(
            split_input[0].filter_('scale', size='uhd2160', force_original_aspect_ratio='increase'),
            fontsize=64
        ).output(f'{name}_3840.mp4', **OUTPUT_OPTIONS),
        # 1920x1080
        add_watermark(
            split_input[1].filter_('scale', size='hd1080', force_original_aspect_ratio='increase'),
            fontsize=32
        ).output(f'{name}_1920.mp4', **OUTPUT_OPTIONS),
        # 960x540
        add_watermark(
            split_input[2].filter_('scale', size='qhd', force_original_aspect_ratio='increase'),
            fontsize=16
        ).output(f'{name}_960.mp4', **OUTPUT_OPTIONS),
    )

    if verbose:
        print('ffmpeg ' + ' '.join(output.get_args()))
        output.view(filename=f'{name}')  # Automatically suffixed with .pdf

    if not dry_run:
        output.run(overwrite_output=True)

    return output
