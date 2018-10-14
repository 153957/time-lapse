import ffmpeg

from .watermark import add_watermark

OUTPUT_OPTIONS = {
    'crf': 20,
    'preset': 'slower',
    'movflags': 'faststart',
    'pix_fmt': 'yuv420p'
}


def create_outputs(input, name, framerate=None, verbose=False, dry_run=False):
    """Create output at multiple sizes

    :param input: ffmpeg input node ready for scaling and conversion.
    :param name: name of the output.
    :param verbose: if True output the ffmpeg CLI command which will be used.
    :param dry_run: if True the command will not be run.

    """
    watermarked_input = add_watermark(
        input.filter_('scale', size='hd1080', force_original_aspect_ratio='increase'),
        fontsize=32
    )

    split_input = watermarked_input.split()

    if framerate:
        output_options = {'r': framerate, **OUTPUT_OPTIONS}
    else:
        output_options = OUTPUT_OPTIONS

    output = ffmpeg.merge_outputs(
        # 1920x1080 (1920x1280)
        split_input[0].output(f'{name}_1920.mp4', **output_options),
        # 960x540 (960x640)
        (
            split_input[1]
            .filter_('scale', size='qhd', force_original_aspect_ratio='increase')
            .output(f'{name}_960.mp4', **output_options)
        )
    )

    if verbose:
        print('ffmpeg ' + ' '.join(output.get_args()))
        output.view(filename=f'{name}')  # Automatically suffixed with .pdf

    if not dry_run:
        output.run(overwrite_output=True)

    return output
