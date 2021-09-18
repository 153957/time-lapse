import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/180430_1_Loch_Lomond/*.tiff',  # APL_022590 - APL_022733
    '/Volumes/Falcon/tl_temp/180430_2_Loch_Lomond/*.tiff',  # APL_022748 - APL_022928
]


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 48, 0, watermark=True, verbose=False, dryrun=False)
