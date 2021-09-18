import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/190429_4_Waterfall/*.tiff',  # APL_049902 - APL_050084
    '/Volumes/Falcon/tl_temp/190429_5_Waterfall/*.tiff',  # APL_050155 - APL_050292
    '/Volumes/Falcon/tl_temp/190429_6_Waterfall/*.tiff',  # APL_050300 - APL_050457
    '/Volumes/Falcon/tl_temp/190429_1_Waterfall/*.tiff',  # APL_049154 - APL_049439
    '/Volumes/Falcon/tl_temp/190429_2_Waterfall/*.tiff',  # APL_049481 - APL_049696
    '/Volumes/Falcon/tl_temp/190429_3_Waterfall/*.tiff',  # APL_049698 - APL_049888
]


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 4, watermark=True, verbose=False, dryrun=False)
