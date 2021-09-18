import ffmpeg

from .watermark import add_watermark

OUTPUT_OPTIONS = {
    'crf': 20,
    'preset': 'slower',
    'movflags': 'faststart',
    'pix_fmt': 'yuv420p'
}


def create_outputs(
    source_input,
    name,
    framerate=None,
    watermark=True,
    verbose=False,
    dryrun=False,
):
    """Create output at multiple sizes (FHD and qHD)

    :param source_input: ffmpeg input node ready for scaling and conversion.
    :param name: name of the output.
    :param watermark: if True the default watermark will be added to the movie,
        if a tuple is provided the contained strings are used for the main an sub lines.
    :param verbose: if True output the ffmpeg CLI command which will be used.
    :param dryrun: if True the command will not be run.

    """

    fhd_input = source_input.filter_('scale', size='hd1080', force_original_aspect_ratio='increase')

    if watermark:
        if watermark is True:
            text = 'Arne de Laat'
            subtext = '153957 Photography'
        else:
            text, subtext = watermark
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
        split_input[0].output(f'{name}.mp4', **output_options),
        # 960x540 (960x640)
        (
            split_input[1]
            .filter_('scale', size='qhd', force_original_aspect_ratio='increase')
            .output(f'{name}_960.mp4', **output_options)
        )
    )

    if verbose:
        print('ffmpeg ' + ' '.join(output.get_args()))
        try:
            output.view(filename=f'{name}')  # Automatically suffixed with .pdf
        except ImportError:
            print('Install graphviz to generate the a signal graph')

    if not dryrun:
        output.global_args('-hide_banner').run(overwrite_output=True)

    return output
