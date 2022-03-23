import os

from time_lapse import output, source

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Jedi/Cache/220323_1_APL/*.tif',  # APL_103712 - APL_103931
# poster: APL_103782


if __name__ == '__main__':
    source_input = (
        source
        .get_input(PATTERN, 24, 0)
        .filter_('tblend', all_mode='lighten', all_opacity=0.33)
        .filter_('tblend', all_mode='lighten', all_opacity=0.33)
    )

    output.create_outputs(source_input, NAME, watermark=True, verbose=False, dryrun=False)
