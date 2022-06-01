import os

import ffmpeg

from time_lapse import output, source

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Crimson/Cache/160605_ADL_Tango/*.tif'  # ADL_183879 - ADL_184093
# poster: ADL_183879

if __name__ == '__main__':
    source_input = (
        source
        .get_input(PATTERN, 24, 0)
        .filter_('tblend', all_mode='darken', all_opacity=0.5)
    )

    output.create_outputs(source_input, NAME, watermark=True, verbose=False, dryrun=False)
