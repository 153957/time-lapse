import os

import ffmpeg

from time_lapse import output, source

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN1 = '/Volumes/Jedi/Cache/220401_1_skydive/*.tif'  # APL_104104 - APL_104314
PATTERN2 = '/Volumes/Jedi/Cache/220401_6_skydive/*.tif'  # APL_105404 - APL_106184
# poster: APL_105558

if __name__ == '__main__':
    input1 = (
        source
        .get_input(PATTERN1, 24, 0)
    )

    input2 = (
        source
        .get_input(PATTERN2, 24, 0)
        .filter_('tblend', all_mode='darken', all_opacity=0.33)
        .filter_('tblend', all_mode='darken', all_opacity=0.33)
    )

    inputs = ffmpeg.concat(input1, input2)

    output.create_outputs(inputs, NAME, watermark=True, verbose=False, dryrun=False)
