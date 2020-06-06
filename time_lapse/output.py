import ffmpeg

from .watermark import add_watermark

OUTPUT_OPTIONS = {
    'crf': 20,
    'preset': 'slower',
    'movflags': 'faststart',
    'pix_fmt': 'yuv420p'
}


def create_outputs(
    input,
    name,
    framerate=None,
    verbose=False,
    dry_run=False,
    watermark=True,
    text='Arne de Laat',
    subtext='153957 Photography',
):
    """Create output at multiple sizes (FHD and qHD)

    :param input: ffmpeg input node ready for scaling and conversion.
    :param name: name of the output.
    :param verbose: if True output the ffmpeg CLI command which will be used.
    :param dry_run: if True the command will not be run.
    :param watermark: if True a watermark will be added to the movie.

    """
    fhd_input = input.filter_('scale', size='hd1080', force_original_aspect_ratio='increase')

    if watermark:
        watermarked_input = add_watermark(fhd_input, text, subtext, fontsize=32)
        split_input = watermarked_input.split()
    else:
        split_input = fhd_input.split()

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
        output.global_args('-hide_banner').run(overwrite_output=True)

    return output
